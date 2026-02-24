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
potion_art = r"""  
   _____
  `.___,'
   (___)
   <   >
    ) (
   /`-.\
  /     \
 / _    _\
:,' `-.' `:
|         |
:         ;
 \       /
  `.___.' 
"""
def roll():
    roll = random.randint(1,100)
    return roll

roll = roll()
sizelist = ["Miniscule" "Tiny", "Average", "Large", "Huge"]
rarlist = ["Common", "Uncommon", "Rare", "Epic", "Legendary", "Mythic"]

speclist = ["Roundhouse", "Low Stab", "Spinjitzu"]
enemy_speclist = ["Back Kick", "Heavy Slam", "Triple Shot"]
weaponlist = ["Kicking Boots", "Dagger", "Longsword"]
potlist = ["Potion of Healing", "Potion of Strength"]

enemylist = ["Nubian Goat", "Zombie", "Skeleton"]
enemy_weaponlist = ["Hooves", "Iron Shovel", "Bow and Arrow"]


roll = random.randint(1,100)

#class 1
class Inventory:
    def __init__(self,weight=0,items=None, gold=None):
        if items is None:
            items = []
            self.items = items
            self.weight = weight
            self.gold = gold

    def add_gold(self,amt):
        self.gold += amt

    def add_item(self,item):
        self.items.append(item)
    
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Removed {item.name} from inventory.")
        else:
            print(f"{item.name} not found in inventory.")
    
    def remove_gold(self, amt):
        self.gold -= amt

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
        print()
class Entity:
    def __init__(self, health, level, xp, size, race, strength):
        self.health = health
        self.level = level
        self.xp = xp
        self.size = size
        self.race = race
        self.strength = strength
        self.inventory = Inventory()
   
    def shop(self):
        print()

    def make_enemy(self):
        enemy = Entity(10 + (self.level * self.level * 4), self.level, 0, random.choice(sizelist), random.choice(enemylist), 1)
        return enemy
    
    def make_enemy_weapon(self, enemy):
        enemy_weapon = Weapon(enemy_weaponlist[enemylist.index(enemy.race)], enemy.health/2, 41, random.choice(rarlist), 1, enemy_speclist[enemylist.index(enemy.race)])
        return enemy_weapon
    
    def checkweight(self):
        weight = 0
        limit = self.level * self.strength
        if limit < 40:
            limit = 40
        if self.inventory.items:
            counter = 0
            print("Inventory: ")
            for item in self.inventory.items:
                counter += 1
                weight += item.weight
                if item.name in weaponlist:
                    print(f"{str(counter)}. {item.name}: {item.damage} damage, {item.durability} durability, {item.weight} weight")
                if item.name in potlist:
                    print(f"{str(counter)}. {item.name}, {item.weight} weight")
        else:
            print(f"Inventory is empty.")
        print(f"Total weight: {weight}")
        while weight > limit:
            print(f"You have exceeded your {limit} kg weight limit!")
            choice = input(f"What item would you like to drop? ").strip().title()
            for item in self.inventory.items:
                #print(self.inventory.items)
                if int(choice) - 1 == self.inventory.items.index(item):
                    self.remove_weapon_from_inventory(item)
                    print(f"You dropped {item.name}.")
            for item in self.inventory.items:
                weight = 0
                weight += item.weight
        return weight


    def potion_use(self, potion):
        if potion in self.inventory.items:
#            print(potion.name)
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
        #self.inventory.display_inventory()
        choice = input("What would you like to do: \n 1: Attack \n 2: Use Potion \n 3: View Inventory \n ").strip().lower()
        if choice == "1":
            wepchoice = input("What weapon would you like to attack with? ").strip().lower()
            for i in self.inventory.items:
                print(self.inventory.items.index(i)+1)
                print(wepchoice)
                if int(wepchoice) == int(self.inventory.items.index(i)+1):
                    self.attack(self.inventory.items[int(wepchoice) - 1], enemy)
        elif choice == "2":
#            print("Yes")
            potchoice = input("What potion would you like to use? ").strip().lower()
#            print(self.inventory.items[int(potchoice) - 1].name)
            for item in self.inventory.items:
#               print(item.name)
                if self.inventory.items[int(potchoice) - 1].name == item.name:
#                   print("YES")
                    self.potion_use(self.inventory.items[int(potchoice) - 1])
        elif choice == "3":
            self.inventory.display_inventory()
            self.choice(enemy)
        else:
            print("You messed up so you get your turn skipped.")

    def xpgain(self, mult):
        gain = random.randint(1,3)
        self.add_gold_to_inventory(gain/3*self.level)
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

            total_damage = weapon.damage + self.strength*weapon.damage*.1

            target.take_damage(total_damage)

            weapon.degrade(self.inventory)

            if target.health <= 0:
                print(f"You killed {target.race}!")
                self.xpgain(2)
        else:
            print("Weapon not in inventory")


    def add_weapon_to_inventory(self,weapon):
        self.inventory.add_item(weapon)
    
    def add_gold_to_inventory(self,amt):
        self.inventory.add_gold(amt)

    def remove_weapon_from_inventory(self,weapon):
        self.inventory.remove_item(weapon)
    
    def remove_gold_from_inventory(self, amt):
        self.inventory.remove_gold(amt)


    def encounter(self):
        if roll <= 20:
            addition = random.choice(weaponlist)
            addition = Weapon(addition, self.level*self.level*random.randint(10, 30) * .1, roll, random.choice(rarlist), self.level * 2 * 10, speclist[weaponlist.index(addition)])
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
###################################               
        if roll <= 40:
            addition = random.choice(potlist)
            addition = Item(addition, 4)
            print(potion_art)
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
    def __init__(self, name, damage, durability, rarity, weight, special):
        self.name = name
        self.damage = damage
        self.durability = durability
        self.rarity = rarity
        self.special = special
        self.weight = weight


    def degrade(self, inventory):
        self.durability -= 1
        print(f"{self.name} durability: {self.durability}")
        if self.durability <= 0:
            print(f"{self.name} broke!")
            inventory.remove(self)

class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
#class 3


class main():
    hero = Entity(20, 1, 0, "large", "You", 1)
    enemy = hero.make_enemy()
    kicking_boots = Weapon("Kicking Boots", 5, 10, "mythical", 15, "roundhouse")
    enemy_weapon = hero.make_enemy_weapon(enemy)
    hero.add_weapon_to_inventory(kicking_boots)
    enemy.add_weapon_to_inventory(enemy_weapon)
#    print(enemy.inventory.items[0].name)
#    print(hero.inventory.items[0].name)

    print("You wake up to find yourself in a cavern, only illuminated by some strage fungi above you.")
    time.sleep(3)
    print("You stand up and walk through the dimly lit space.")
    #print(roll)
    time.sleep(2)
    print("You pick up a heavy backpack that was sitting on the wall.")
    time.sleep(2)
    print("Next to the backpack you find 3 gold.")
    hero.encounter()
    time.sleep(3)
    hero.checkweight()
    time.sleep(6)


    print(f"{enemy.describe()}")
    time.sleep(3)

    hero.checkweight()
    time.sleep(2)

    while enemy.health > 0:
        hero.choice(enemy)
        if enemy.health <= 0:
            break
        enemy.attack(enemy_weapon, hero)



if __name__ == "__main__":
    main()