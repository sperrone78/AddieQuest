class Weapon:
    def __init__(self, name, weapon_type, quality="Rusty", damage=1, weight=1, two_handed=False, cost=1):
        self.name = name
        self.weapon_type = weapon_type
        self.quality = quality
        self.damage = damage
        self.weight = weight
        self.two_handed = two_handed
        self.cost = cost

    def __str__(self):
        return_str = str(f'''Weapon Name: {self.name}
        Weapon Type: {self.weapon_type}
        Weapon Quality: {self.quality}
        Damage: {self.damage}''')
        return return_str

    def reprJSON(self):
        return dict(weapon_type=self.weapon_type, name=self.name, quality=self.quality,
                    damage=self.damage, weight=self.weight, two_handed=self.two_handed,
                    cost=self.cost)
