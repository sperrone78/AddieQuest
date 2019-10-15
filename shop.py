from npc import NPC
from weapon import Weapon
from armor import Armor
from item import Item
import json


class Shop:
    def __init__(self, shop_type="General", shop_keeper=None, items_for_sale=[]):
        if shop_keeper is None:
            self.create_shop_keeper()
        else:
            self.shop_keeper = shop_keeper
        self.shop_type = shop_type
        self.items_for_sale = items_for_sale
        self.load_inventory()

    def load_inventory(self):
        print("Loading Store...")
        if self.shop_type == "Weapon":
            with open("./res/weapon.JSON", "r") as file:
                data = json.load(file)
            for weapon in data['weapons']:
                self.items_for_sale.append(Weapon(weapon['weapon_type'], weapon['name'], weapon['quality'],
                                                  weapon['damage'], weapon['weight'], weapon['two_handed'],
                                                  weapon['cost']))
        elif self.shop_type == "Armor":
            with open("./res/armor.JSON", "r") as file:
                data = json.load(file)
            for armor in data['armors']:
                self.items_for_sale.append(Armor(armor['armor_type'], armor['name'], armor['quality'],
                                                 armor['soak'], armor['weight'], armor['equipment_slot'],
                                                 armor['cost']))
        elif self.shop_type == "General":
            with open("./res/item.JSON", "r") as file:
                data = json.load(file)
            for item in data['items']:
                self.items_for_sale.append(Item(item['name'], item['weight'], item['cost']))
        else:
            print("Unknown Shop Type")

    def list_items(self):
        print(f"Items for sale: {self.items_for_sale}")

    def __str__(self):
        return_str = str(f'''Shop Name: {self.shop_keeper.name}'s {self.shop_type} Shop''')
        return return_str

    def create_shop_keeper(self):
        print('Enter the Shopkeepers name: ')
        npc_name = input()
        self.shop_keeper = NPC(npc_name, "Shop Keeper")

    def reprJSON(self):
        return dict(shop_keeper=self.shop_keeper, shop_type=self.shop_type, items_for_sale=self.items_for_sale)