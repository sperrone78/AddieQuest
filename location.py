class Location:
    def __init__(self, name, location_type):
        self.name = name
        self.location_type = location_type

    def __str__(self):
        print(f'Location Name: {self.name}')

    def reprJSON(self):
        return dict(name=self.name, location_type=self.location_type)
# {"Armor Shop": "shop", "Weapon Shop": "shop", "General Shop": "shop", "Home": "home",
#                           "Dungeon": "dangerous", "Forest": "dangerous"}
