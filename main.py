import json
from player import Player
from npc import NPC
from weapon import Weapon
from armor import Armor
from game import Game
from backpack import Backpack
from globe import Globe
from shop import Shop


def save_game(game):
    game_JSON_dump = json.dumps(game.reprJSON(), cls=ComplexEncoder)

    with open("./game_save.json", "w") as file:
        file.write(game_JSON_dump)
        file.close()


def create_equip():
    weapon_dict = []
    weapon_dict.append(create_weapon())
    weapon_dict.append(create_weapon())
    weapon_dump = json.dumps(weapon_dict, cls=ComplexEncoder)

    armor_dict = []
    armor_dict.append(create_armor())
    armor_dict.append(create_armor())
    armor_dump = json.dumps(armor_dict, cls=ComplexEncoder)

    with open("./weapon.json", "w") as file:
        file.write(weapon_dump)
        file.close()

    with open("./armor.json", "w") as file:
        file.write(armor_dump)
        file.close()


def load_game():
    with open("./game_save.JSON", "r") as file:
        data = json.load(file)
        print(f"Welcome back {data['player']['name']}")

    loaded_backpack = Backpack(data['player']['backpack']['max_slots'],
                               data['player']['backpack']['filled_slots'],
                               data['player']['backpack']['items_inside'])
    # create each item - need to create an "equipment" class
    loaded_player = Player(data['player']['name'], loaded_backpack,
                           data['player']['gold'], data['player']['current_health'],
                           data['player']['max_health'], data['player']['current_location'])
    loaded_globe = Globe(data['globe']['locations'], data['globe']['found_locations'])

    loaded_shops = ['']
    for shop in data['shops']:
        shop_keeper = NPC(shop['shop_keeper']['name'], shop['shop_keeper']['npc_type'])
        loaded_shops.append(Shop(shop['shop_type'], shop_keeper, []))
        # I think I can just load empty set for item_for_sale and have them load each game restart

    game = Game(loaded_player, loaded_shops, loaded_globe)
    return game


def create_armor():
    print("What armor is he selling?")
    armor_type = input()
    print("What's it's name?")
    armor_name = input()
    new_armor = Armor(armor_name, armor_type)
    return new_armor


def create_weapon():
    print("What weapon is he selling?")
    weapon_type = input()
    print("What's it's name?")
    weapon_name = input()
    new_weapon = Weapon(weapon_name, weapon_type)
    return new_weapon


def run_game(game):
    while True:
        player = game.player
        backpack = player.backpack
        print("What do you want to do? (type 'help' for a list of commands): ")
        current_option = input()

        if current_option == 'look':
            # Need to create a JSON file with stuff the shop keeper sells and load it
            print(f"{player.name} looks around the {player.current_location}")
        elif current_option == 'backpack':
            print(f'{backpack}')
        elif current_option == 'status':
            print(f"{player}")
        elif current_option == 'save':
            print("Saving Game")
            save_game(game)
        elif current_option == 'move':
            game.move_player()
        elif current_option == 'help':
            print("Command options: save, quit, shop, status, backpack, move, look")
        elif current_option == 'money':
            player.gold += 10
        elif current_option == 'create':
            create_equip()
        else:
            print("BREAK!")
            break


def main():
    print('''Welcome to the Game!
          Please Choose an Option:
          1 - New Game
          2 - Load Game
          3 - Exit Game''')
    main_screen_option = input()

    if main_screen_option == "1":
        print("New Game")
        game = Game()
        run_game(game)

    elif main_screen_option == "2":
        print("Load Game")
        game = load_game()
        run_game(game)

    else:
        print("Goodbye!")
        exit()


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'reprJSON'):
            return obj.reprJSON()
        else:
            return json.JSONEncoder.default(self, obj)


if __name__ == "__main__":
    main()
