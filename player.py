from backpack import Backpack


class Player:
    def __init__(self, name=None, backpack=Backpack()):
        self.name = name
        self.backpack = backpack
        print(f'Creating new player named: {name}')

    def talk(self):
        print(f'{self.name} says hello world')

    def reprJSON(self):
        return dict(name=self.name, backpack=self.backpack)

    def __str__(self):
        return_str = str(f'''
        Character Name: {self.name}
        Character Class: Warrior
        Character Race: Elf''')
        return return_str
