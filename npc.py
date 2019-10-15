class NPC:
    def __init__(self, name, npc_type):
        self.name = name
        self.npc_type = npc_type

    def talk(self):
        print(f'{self.name} is a {self.npc_type}')

    def reprJSON(self):
        return dict(name=self.name, npc_type=self.npc_type)
