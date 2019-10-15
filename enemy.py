class Enemy:
    def __init__(self, name, current_health=10, max_health=10, current_mana=10, max_mana=10, damage=1, armor=1,
                 description="Enemy", coordinate=4):
        self.name = name
        self.current_health = current_health
        self.max_health = max_health
        self.current_mana = current_mana
        self.max_mana = max_mana
        self.damage = damage
        self.armor = armor
        self.description = description
        self.coordinate = coordinate

    def attack(self):
        print("I hit you")

    def talk(self):
        print("I'm a generic bad guy!")

    def move(self, new_coordinate):
        print(f"{self.name} moves from {self.coordinate} to {new_coordinate}")

    def __str__(self):
        return_str = str(f'''Enemy Name: {self.name}
        Description: {self.description}
        Damage = {self.damage}
        Armor = {self.armor}    
        Health = {self.current_health} / {self.max_health}
        Mana = {self.current_mana} / {self.max_mana}
        Location = {self.coordinate}''')
        return return_str

    def reprJSON(self):
        return dict(name=self.name, current_health=self.current_health, max_health=self.max_health,
                    current_mana=self.current_mana, max_mana=self.max_mana, description=self.description,
                    coordinate=self.coordinate, damage=self.damage, armor=self.armor)
