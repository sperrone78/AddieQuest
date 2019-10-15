from location import Location
import json


class Globe:
    def __init__(self, locations=None, current_location=0):
        if locations is None:
            self.create_locations()
        else:
            self.locations = locations
        self.current_location = current_location

    def create_locations(self):
        # Load locations.json
        print("Loading Locations")
        self.locations = {}
        coordinate = 0
        with open("./res/globe.JSON", "r") as file:
            data = json.load(file)
        for location in data['globe']:
            # print(f"name = {location['name']} and type = {location['location_type']}")
            self.locations[coordinate] = (Location(location['name'], location['location_type']))
            coordinate += 1

    def reprJSON(self):
        return dict(locations=self.locations, current_location=self.current_location)
