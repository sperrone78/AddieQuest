class Weapon:
    def __init__(self, name, weapon_type):
        self.name = name
        self.weapon_type = weapon_type

    def getinfo(self):
        # print(f'opening file for {self.weapon_type}')
        return self.weapon_type

    def reprJSON(self):
        return dict(weapon_type=self.weapon_type, name=self.name)
