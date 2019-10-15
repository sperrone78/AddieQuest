from player import Player
from globe import Globe
from shop import Shop


class Game:
    def __init__(self, player=None, shops=None, globe=None):
        print(f'Welcome to the game!')
        if player is None:
            self.create_player()
        else:
            self.player = player
        if globe is None:
            self.create_globe()
        else:
            self.globe = globe
        if shops is None:
            self.create_shops()
        else:
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
            if new_location == "locations":
                for loc in self.globe.locations.values():
                    print(f"You can travel to: {loc.name}")
            else:
                coordinate = 0
                for loc in self.globe.locations.values():
                    # print(f'checking {loc.name} against {new_location}')
                    if loc.name == new_location:
                        self.player.current_coordinate = coordinate
                        print(f'{self.player.name} moves to {new_location} (coordinate: {coordinate})')
                        break
                    else:
                        # print(f"{new_location} is not a valid location to move to!")
                        coordinate += 1

    def reprJSON(self):
        return dict(player=self.player, shops=self.shops, globe=self.globe)

    def quit(self):
        exit()
