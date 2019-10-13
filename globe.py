class Globe:
    def __init__(self, locations=("Armor Shop", "Weapon Shop", "General Shop", "Home", "Dungeon", "Forest"), found_locations=["Home"]):
        self.locations = locations
        self.found_locations = found_locations

    def reprJSON(self):
        return dict(locations=self.locations, found_locations=self.found_locations)
