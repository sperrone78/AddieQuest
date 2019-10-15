from weapon import Weapon
from armor import Armor
import json


def create_equip():
    weapon_dict = []
    weapon_dict.append(create_weapon())
    weapon_dict.append(create_weapon())
    weapon_dump = json.dumps(weapon_dict, cls=ComplexEncoder)

    armor_dict = []
    armor_dict.append(create_armor())
    armor_dict.append(create_armor())
    armor_dump = json.dumps(armor_dict, cls=ComplexEncoder)

    with open("./weapon.json", "w") as file:
        file.write(weapon_dump)
        file.close()

    with open("./armor.json", "w") as file:
        file.write(armor_dump)
        file.close()


def create_armor():
    print("What armor is he selling?")
    armor_type = input()
    print("What's it's name?")
    armor_name = input()
    new_armor = Armor(armor_name, armor_type)
    return new_armor


def create_weapon():
    print("What weapon is he selling?")
    weapon_type = input()
    print("What's it's name?")
    weapon_name = input()
    new_weapon = Weapon(weapon_name, weapon_type)
    return new_weapon
