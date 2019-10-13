class Armor:
    def __init__(self, name, armor_type, quality="Rusty", soak=1, weight=1, equipment_slot="Chest", cost=1):
        self.name = name
        self.armor_type = armor_type
        self.quality = quality
        self.soak = soak
        self.weight = weight
        self.equipment_slot = equipment_slot
        self.cost = cost

    def __str__(self):
        return_str = str(f'''Armor Name: {self.name}
        Armor Type: {self.armor_type}
        Armor Quality: {self.quality}
        Damage Soak: {self.soak}''')
        return return_str

    def reprJSON(self):
        return dict(armor_type=self.armor_type, name=self.name, quality=self.quality,
                    soak=self.soak, weight=self.weight, equipment_slot=self.equipment_slot,
                    cost=self.cost)
