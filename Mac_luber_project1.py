import random
import time

dagger_art = r"""
  / \
  | |
  | |
  |.|
  |.|
  |:|
  |:|
`--8--'
   8
   O
"""
boots_art = r"""
     ._......     
     |X/.*| |     
     |X/+ | |     
     |X/* | |     
____/     ; ;       
\_____/|_/_/
"""
longsword_art = r"""
     /\
    // \
    || |
    || |
    || |
    || |
    || |
    || |
 __ || | __
/___||_|___\
     ww
     MM
    _MM_
   (&<>&)
    ~~~~
"""

def roll():
    roll = random.randint(1,100)
    return roll

roll = roll()

rarlist = ["Common", "Uncommon", "Rare", "Epic", "Legendary", "Mythic"]

speclist = ["Roundhouse", "Low Stab", "Spinjitzu"]
weaponlist = ["Kicking Boots", "Dagger", "Longsword"]
potlist = ["Potion of Healing", "Potion of Strength"]

enemylist = ["Nubian Goat", "Zombie", "Skeleton"]


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
            print(f"Removed {item.name} from inventory.")
        else:
            print(f"{item.name} not found in inventory.")

    def display_inventory(self):
        if self.items:
            counter = 0
            print("Inventory: ")
            for item in self.items:
                counter += 1
                if item.name in weaponlist:
                    print(f"{str(counter)}. {item.name}: {item.damage} damage, {item.durability} durability")
                if item.name in potlist:
                    print(f"{str(counter)}. {item.name}")
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
   
#    def make_enemy(self):
        

    def potion_use(self, potion):
        if potion in self.inventory.items:
            if potion.name == "Potion of Healing":
                self.health += self.level * 3/2
                print(f"You used potion of healing. Hero now has {self.health} hp.")
                self.inventory.remove_item(potion)
            if potion.name == "Potion of Strength":
              self.strength += self.level * 1/2
              print(f"You used Potion of Strength. You now have {self.strength} strength.")
              self.inventory.remove_item(potion)
        else:
            print("Potion not in inventory")

    def choice(self, enemy):
        #Add more
        self.inventory.display_inventory()
        choice = input("What would you like to do: \n 1: Attack \n 2: Use Potion \n").strip().lower()
        if choice == "1":
            wepchoice = input("What weapon would you like to attack with? ").strip().lower()
            for i in self.inventory.items:
                print(self.inventory.items.index(i)+1)
                print(wepchoice)
                if int(wepchoice) == int(self.inventory.items.index(i)+1):
                    self.attack(self.inventory.items[int(wepchoice) - 1], enemy)
        elif choice == "2":
            potchoice = input("What potion would you like to use? ").strip().lower()
#            print(self.inventory.items[int(potchoice) - 1].name)
            for item in self.inventory.items:
                if potchoice == item.name:
                    self.potion_use(self.inventory.items[int(potchoice) - 1])
        else:
            print("You messed up so you get your turn skipped.")

    def xpgain(self, mult):
        gain = random.randint(1,3)
        gain = gain * ((mult/100)+2)
        round(gain, 1)
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
            return f"{self.race} died!"
    

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
            if addition.name == "Longsword":
                print(longsword_art)
            elif addition.name == "Kicking Boots":
                print(boots_art)
            elif addition.name == "Dagger":
                print(dagger_art)
            print(f"You found {addition.name}: \n - {addition.damage} damage \n - {addition.durability} durability \n - {addition.rarity} \n - Special Ability: {addition.special} ")
            decision = input("Do you want to add the weapon to inventory? ").strip().lower()
            if decision == "yes":
                self.add_weapon_to_inventory(addition)
                print("Weapon added to inventory.")
            else:
                print("Weapon not added to inventory.")
        elif roll <= 40:
            addition = random.choice(potlist)
            addition = Item(addition)
            if addition.name == "Potion of Healing":
                decision = input("You have found a potion of healing(Heals you based on your level)! Would you like to add it to your inventory? ").strip().lower()
                if decision == "yes":
                    self.add_weapon_to_inventory(addition)
                    print("Potion added to inventory.")
                else:
                    print("Potion not added to inventory.")
            if addition.name == "Potion of Strength":
                decision = input("You have found a potion of strength(Permenantly makes you stronger)! Would you like to add it to your inventory? ").strip().lower()
                if decision == "yes":
                    self.add_weapon_to_inventory(addition)
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

class Item:
    def __init__(self, name):
        self.name = name
#class 3


class main():
    hero = Entity(20, 1, 0, "large", "Hero", 1)
    enemy = Entity(15, 1, 0, "tiny", "Goat", 1)
    kicking_boots = Weapon("Kicking Boots", 5, 10, "mythical", "roundhouse")
    enemy_weapon = Weapon("Hooves", 1, 15, "common", "ram")
    hero.add_weapon_to_inventory(kicking_boots)
    enemy.add_weapon_to_inventory(enemy_weapon)
#    print(enemy.inventory.items[0].name)
#   print(hero.inventory.items[0].name)


    print(roll)
    hero.encounter()


    #print(f"Behold your mighty hero!!! {hero.describe()}")
    #print(f"{enemy.describe()}")

    while enemy.health > 0:
        hero.choice(enemy)
        if enemy.health <= 0:
            break
        enemy.attack(enemy_weapon, hero)



if __name__ == "__main__":
    main()