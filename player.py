from backpack import Backpack


class Player:
    def __init__(self, name=None, backpack=Backpack(), gold=0,
                 current_health=10, max_health=10, current_location="Home"):
        self.name = name
        self.backpack = backpack
        self.gold = gold
        self.current_health = current_health
        self.max_health = max_health
        self.current_location = current_location
        print(f'Creating new player named: {name}')

    def reprJSON(self):
        return dict(name=self.name, backpack=self.backpack, gold=self.gold,
                    current_health=self.current_health, max_health=self.max_health,
                    current_location=self.current_location)

    def __str__(self):
        return_str = str(f'''
        Character Name: {self.name}
        Character Class: Warrior
        Character Race: Elf
        Gold = {self.gold} pieces
        Health = {self.current_health} / {self.max_health}
        Location = {self.current_location}''')
        return return_str
