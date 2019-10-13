from player import Player
from globe import Globe
from shop import Shop


class Game:
    def __init__(self, player=None, shops=None, globe=None):
        print(f'Welcome to the game!')
        if player is None: # New Game
            self.create_player()
            self.create_globe()
            self.create_shops()
        else: # Loaded Game
            self.player = player
            self.globe = globe
            self.shops = shops

    def create_player(self):
        print('Enter your name: ')
        name = input()
        self.player = Player(name)

    def create_shops(self):
        self.shops = []
        self.shops.append(Shop("General"))
        self.shops.append(Shop("Armor"))
        self.shops.append(Shop("Weapon"))

    def create_globe(self):
        print("Creating Map")
        self.globe = Globe()

    def move_player(self):
        while True:
            print('Where do you want to move to? (Type "locations" for a list of options)')
            new_location = input()
            if new_location in self.globe.locations:
                self.player.current_location = new_location
                print(f'{self.player.name} moves to {new_location}')
                break
            elif new_location == "locations":
                print(f"You can travel to: {self.globe.locations}")
            else:
                print(f"{new_location} is not a valid location to move to!")

    def reprJSON(self):
        return dict(player=self.player, shops=self.shops, globe=self.globe)

    def quit(self):
        exit()
