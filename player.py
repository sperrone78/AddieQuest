from backpack import Backpack


class Player:
    def __init__(self, name=None, backpack=Backpack(), gold=0,
                 current_health=100, max_health=100, current_coordinate=0,
                 damage=10, armor=10):
        self.name = name
        self.backpack = backpack
        self.gold = gold
        self.current_health = current_health
        self.max_health = max_health
        self.current_coordinate = current_coordinate
        self.damage = damage
        self.armor = armor
        print(f'Creating new player named: {name}')

    def reprJSON(self):
        return dict(name=self.name, backpack=self.backpack, gold=self.gold,
                    current_health=self.current_health, max_health=self.max_health,
                    current_coordinate=self.current_coordinate, damage=self.damage, armor=self.armor)

    def __str__(self):
        return_str = str(f'''
        Character Name: {self.name}
        Character Class: Warrior
        Character Race: Elf
        Damage = {self.damage} / Armor = {self.armor}
        Gold = {self.gold} pieces
        Health = {self.current_health} / {self.max_health}''')
        return return_str
