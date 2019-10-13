class Item:
    def __init__(self, name, weight=1, cost=1):
        self.name = name
        self.weight = weight
        self.cost = cost

    def __str__(self):
        return_str = str(f'''Item Name: {self.name}''')
        return return_str

    def reprJSON(self):
        return dict(name=self.name, weight=self.weight, cost=self.cost)