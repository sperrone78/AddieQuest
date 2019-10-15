import json
import random
from player import Player
from npc import NPC
# from weapon import Weapon
# from armor import Armor
from game import Game
from backpack import Backpack
from globe import Globe
from shop import Shop
from location import Location
from enemy import Enemy
from ogre import Ogre


def save_game(game):
    game_JSON_dump = json.dumps(game.reprJSON(), cls=ComplexEncoder)

    with open("./res/game_save.json", "w") as file:
        file.write(game_JSON_dump)
        file.close()


def load_game():
    with open("./res/game_save.JSON", "r") as file:
        data = json.load(file)
        print(f"Welcome back {data['player']['name']}")

    loaded_backpack = Backpack(data['player']['backpack']['max_slots'],
                               data['player']['backpack']['filled_slots'],
                               data['player']['backpack']['items_inside'])

    loaded_player = Player(data['player']['name'], loaded_backpack,
                           data['player']['gold'], data['player']['current_health'],
                           data['player']['max_health'], data['player']['current_coordinate'])

    loaded_shops = ['']
    for shop in data['shops']:
        shop_keeper = NPC(shop['shop_keeper']['name'], shop['shop_keeper']['npc_type'])
        loaded_shops.append(Shop(shop['shop_type'], shop_keeper, []))
        # I think I can just load empty set for item_for_sale and have them load each game restart
        # I can probably not load the equipment into the game JSON - but I'll leave it for now

    game = Game(loaded_player, loaded_shops)
    return game


def fight(game):
    print("I'm in the fight module")
    shrek = Ogre("Shrek", 100, 100, 0, 0, 10, 10, "Ogres are like onions...")
    print(shrek)
    shrek.talk()
    dragon = Enemy("Smaug", 1000, 1000, 100, 100, 1000, 100, "Stay out of his mountain.")
    print(dragon)
    dragon.talk()

    player = game.player
    while True:
        print("Combat Round!")
        print(f"{player.name}: {player.current_health}/{player.max_health} HP")
        print(f"{shrek.name}: {shrek.current_health}/{shrek.max_health} HP")

        # need to make this random with (min damage, max damage) as the parameters.
        # Min/Max calc'd off a base damage (min/max) + weapon damage
        # Base Min/Max goes up with strength
        # Can add in crits later (max roll gets "crit" - with more agility the magic number goes down)

        player_ran = random.randint(1, 10)
        enemy_ran = random.randint(1, 10)

        # Need to add "speed" to player and enemy to see who goes first.  Also helps player flee

        print("Attack, Defend, or Flee?")
        combat_choice = input().lower()
        if combat_choice == 'attack':
            print("Attack!!")
            player_damage_taken = shrek.damage + enemy_ran
            player_damage_given = player.damage + player_ran
            print(f'Player does {player_damage_given} damage')
            print(f'{shrek.name} does {player_damage_taken} damage')
            if player.current_health > player_damage_taken:
                player.current_health -= player_damage_taken
            else:
                print("You Died")
                # Need to put in death stuff
                player.current_health = 0
                break

            if shrek.current_health > player_damage_given:
                shrek.current_health -= player_damage_given
            else:
                print(f"You have defeated the evil {shrek.name}")
                # Need to put loot in here
                # Need to put in experience gain here also
                break
        elif combat_choice == 'defend':
            print("Block!")
            # Need to add a block formula if player has a shield -
            # Would a player even want to block? Maybe if enemy is winding up a big hit?
        elif combat_choice == 'flee':
            if player_ran >= enemy_ran:
                print("RUN AWAY!")
                break
            else:
                print(f"{shrek.name} caught you trying to flee!")
                player_damage_taken = shrek.damage + enemy_ran
                print(f'{shrek.name} does {player_damage_taken} damage')
                if player.current_health > player_damage_taken:
                    player.current_health -= player_damage_taken
                else:
                    print("You Died")
                    # Need to put in death stuff
                    # Probably just make this a function - so I don't have the same code in 2 places
                    player.current_health = 0
                    break
        # Need to add in a magic option once I add spells - oi vey
        # maybe a float between .5 and 1.5?


def run_game(game):
    while True:
        player = game.player
        backpack = player.backpack

        current_location = game.globe.locations[player.current_coordinate]
        # Need to make this whole menu contextual based on location
        if current_location.location_type == "home":
            print("Welcome Home")

        print("What do you want to do? (type 'help' for a list of commands): ")
        current_option = input()

        if current_option == 'look':
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
        elif current_option == 'fight':
            fight(game)
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
