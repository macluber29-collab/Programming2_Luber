import random
import time

rarlist = ["Common", "Uncommon", "Rare", "Epic", "Legendary", "Mythic"]

speclist = ["Roundhouse", "Low Stab", "Spinjitzu"]
weaponlist = ["Kicking Boots", "Dagger", "Longsword"]
potlist = ["Potion of Healing", "Potion of Strength"]

roll = random.randint(1,100)

#class 1
class Inventory:
    def __init__(self,items=None):
        if items is None:
            items = []
            self.items = items
    
    def add_item(self,item):
        self.items.append(item)
    
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Remove {item.name} from inventory.")
        else:
            print(f"{item.name} not found in inventory.")

    def display_inventory(self):
        if self.items:
            print("Inventory: ")
            for item in self.items:
                print(f"- {item.name}")
        else:
            print(f"Inventory is empty.")
class Entity:
    def __init__(self, health, level, xp, size, race, strength):
        self.health = health
        self.level = level
        self.xp = xp
        self.size = size
        self.race = race
        self.strength = strength
        self.inventory = Inventory()
   

    def potion_use(self, potion):
        if potion in self.inventory.items:
            if potion == "Potion of Healing":
                self.hp += self.level * 3/2
            if potion == "Potion of Strength":
              self.strength += self.level * 1/2


    def xpgain(self, mult):
        gain = random.randint(1,3)
        gain = gain * ((mult/100)+2)
        self.xp += gain
        requirement = self.level * 2
        while self.xp >= requirement:
            self.level += 1
            print(f"You leveled up to level {self.level}")
            requirement = self.level*2
            round(self.xp)
        print(f"You now have {self.xp} xp out of {requirement} xp required for level {self.level + 1}")


    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.race} now has {self.health} hp.")
        if self.health <= 0:
            return "{self.race} died!"
    

    def describe(self):
        return f"You see a {self.race} that is {self.size} and has {self.strength} strength and is level {self.level} and has {self.health} hp"


    def attack(self, weapon, target):
        if weapon in self.inventory.items:
            print(f"{self.race} attacks {target.race} with {weapon.name}.")

            total_damage = weapon.damage + self.strength

            target.take_damage(total_damage)

            weapon.degrade(self.inventory)

            if target.health <= 0:
                print(f"You killed {target.race}!")
                self.xpgain(2)
        else:
            print("Weapon not in inventory")


    def add_weapon_to_inventory(self,weapon):
        self.inventory.add_item(weapon)
        print(f"{self.race} equips {weapon.name}.")

    def remove_weapon_from_inventory(self,weapon):
        self.inventory.remove_item(weapon)
        print(f"{self.race} unequips {weapon.name}.")


    def encounter(self):
        if roll <= 20:
            addition = random.choice(weaponlist)
            addition = Weapon(addition, self.level * 2, roll, random.choice(rarlist), speclist[weaponlist.index(addition)])
            print(f"You found {addition.name}: \n - {addition.damage} damage \n - {addition.durability} durability \n - {addition.rarity} \n - Special Ability: {addition.special} ")
            decision = input("Do you want to add the weapon to inventory? ").strip().lower()
            if decision == "yes":
                self.inventory.items.append(addition)
                print("Weapon added to inventory.")
            else:
                print("Weapon not added to inventory.")
        elif roll <= 40:
            addition = random.choice(potlist)
            if addition == "Potion of Healing":
                decision = input("You have found a potion of healing(Heals you based on your level)! Would you like to add it to your inventory?").strip().lower()
                if decision == "yes":
                    self.inventory.items.append(addition)
                    print("Potion added to inventory.")
                else:
                    print("Potion not added to inventory.")
            if addition == "Potion of Strength":
                decision = input("You have found a potion of healing(Heals you based on your level)! Would you like to add it to your inventory?").strip().lower()
                if decision == "yes":
                    self.inventory.items.append(addition)
                    print("Potion added to inventory.")
                else:
                    print("Potion not added to inventory.")


class Weapon:
    def __init__(self, name, damage, durability, rarity, special):
        self.name = name
        self.damage = damage
        self.durability = durability
        self.rarity = rarity
        self.special = special


    def degrade(self, inventory):
        self.durability -= 1
        print(f"{self.name} durability: {self.durability}")
        if self.durability <= 0:
            print(f"{self.name} broke!")
            inventory.remove(self)




#class 3


class main():
    hero = Entity(20, 1, 0, "large", "Hero", 1)
    enemy = Entity(15, 1, 0, "tiny", "Goat", 1)
    kicking_boots = Weapon("Kicking Boots", 15, 10, "mythical", "roundhouse")
    hooves = Weapon("Hooves", 1, 15, "common", "ram")
    hero.add_weapon_to_inventory(kicking_boots)
    enemy.add_weapon_to_inventory(hooves)
#    print(enemy.inventory.items[0].name)
#   print(hero.inventory.items[0].name)

    print(roll)
    hero.encounter()

    hero.inventory.display_inventory()

    #print(f"Behold your mighty hero!!! {hero.describe()}")
    #print(f"{enemy.describe()}")
   
    enemy.attack(hooves, hero)

    hero.attack(kicking_boots, enemy)



if __name__ == "__main__":
    main()