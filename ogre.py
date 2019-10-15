from enemy import Enemy


class Ogre(Enemy):
    def attack(self):
        print("I hit like an ogre")

    def talk(self):
        print(f"{self.name} says: I'm an Ogre!")
