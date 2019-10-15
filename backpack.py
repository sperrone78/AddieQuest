class Backpack:
    def __init__(self, max_slots=20, filled_slots=1, items_inside=["apple"]):
        print(f"Creating new backpack")
        self.max_slots = max_slots
        self.filled_slots = filled_slots
        self.items_inside = items_inside

    def add_item(self, obj):
        if self.filled_slots < self.max_slots:
            self.items_inside.append(obj)
            self.filled_slots += 1

    def reprJSON(self):
        return dict(max_slots=self.max_slots, filled_slots=self.filled_slots, items_inside=self.items_inside)

    def __str__(self):
        return_str = str(f'''
        Backpack Space: {self.filled_slots} / {self.max_slots}
        Backpack Items: {self.items_inside}''')
        return return_str


