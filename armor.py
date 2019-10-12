class Armor:
    def __init__(self, name, armor_type):
        self.armor_type = armor_type
        self.name = name

    def reprJSON(self):
        return dict(armor_type=self.armor_type,name=self.name)
