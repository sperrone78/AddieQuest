from player import Player
from npc import NPC


class Game:
    def __init__(self, player=None, shop_keeper=None):
        print(f'Welcome to the game!')
        if player is None: # New Game
            self.create_player()
            self.create_npc()
        else: # Loaded Game
            self.player = player
            self.shop_keeper = shop_keeper

    def create_player(self):
        print('Enter your name: ')
        name = input()
        self.player = Player(name)
        self.player.talk()

    def create_npc(self):
        print('Enter the Shopkeepers name: ')
        npc_name = input()
        self.shop_keeper = NPC(npc_name, "Shop Keeper")

    def reprJSON(self):
        return dict(player=self.player, shop_keeper=self.shop_keeper)

    def quit(self):
        exit()
