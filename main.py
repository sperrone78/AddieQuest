import json
from player import Player
from npc import NPC
from weapon import Weapon
from armor import Armor
from game import Game
from backpack import Backpack


def save_game(game):
    game_JSON_dump = json.dumps(game.reprJSON(), cls=ComplexEncoder)

    with open("./game_save.json", "w") as file:
        file.write(game_JSON_dump)
        file.close()


def load_game():
    with open("./game_save.JSON", "r") as file:
        data = json.load(file)
        print(f"Welcome back {data['player']['name']}")

    loaded_shop_keeper = NPC(data['shop_keeper']['name'], data['shop_keeper']['npc_type'])
    loaded_backpack = Backpack(data['player']['backpack']['max_slots'],
                               data['player']['backpack']['filled_slots'],
                               data['player']['backpack']['items_inside'])
    # create each item - need to create an "equipment" class
    loaded_player = Player(data['player']['name'], loaded_backpack)
    # loaded_map = Map()

    game = Game(loaded_player, loaded_shop_keeper)
    return game


def run_game(game):
    player = game.player
    #player.talk()
    backpack = player.backpack
    print(f'Backpack Contents = {backpack.items_inside}')

    while True:
        print("What do you want to do? (type 'help' for a list of commands): ")
        current_option = input()

        # commands = {
        #     'quit': game.quit,
        #     'help': "game.help",
        #     'status': "player.status",
        #     'backpack': backpack.show_contents(),
        #     'attack': "player.attack",
        #     'shop': "player.shop",
        #     'print': print(f'hello world'),
        #     'save': save_game(game)
        # }

        # print(f'command given = {current_option} which should run {commands[current_option]}')
        # if current_option in commands.keys():
        #     print(f'I found your command! {current_option} and now I will {commands[current_option]}')
        #     commands[current_option]

        if current_option == ("1" or 'shop'):
            # Need to create a JSON file with stuff the shop keeper sells and load it
            print("Looking at the shop")
        elif current_option == ('2' or 'backpack'):
            print(f'{backpack}')
            # need to create a backpack tostring
        elif current_option == ('3' or 'status'):
            print(f"{player}")
            # need to create a player tostring
        elif current_option == ('4' or 'save'):
            save_game(game)
        elif current_option == 'help':
            print("Command options: save, quit, shop, status, backpack")
        else:
            break

        # print("What weapon is he selling?")
        # weapon_type = input()
        # print("What's it's name?")
        # weapon_name = input()
        # new_weapon = Weapon(weapon_name, weapon_type)
        # print(f'He sells a {new_weapon.getinfo()} named {new_weapon.name}')
        #
        # print("What armor is he selling?")
        # armor_type = input()
        # print("What's it's name?")
        # armor_name = input()
        # new_armor = Armor(armor_name, armor_type)
        # print(f'He sells a {new_armor.armor_type} called {new_armor.name}')
        #
        # backpack.add_item(new_weapon)
        # backpack.add_item(new_armor)


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
        exit();


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'reprJSON'):
            return obj.reprJSON()
        else:
            return json.JSONEncoder.default(self, obj)


if __name__ == "__main__":
    main()
