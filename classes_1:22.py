import random
import time

#class 1
class Entity:
    def __init__(self, health, level, xp, size, race, strength):
        self.health = health
        self.level = level
        self.xp = xp
        self.size = size
        self.race = race
        self.strength = strength
   
    def xpgain(self, mult):
        gain = random.randint(1,3)
        gain = gain * ((mult/100)+2)
        self.xp += gain
        requirement = self.level * 2
        while self.xp >= requirement:
            self.level += 1
            print(f"You leveled up to level {self.level}")
            requirement = self.level*2

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.race} now has {self.health} hp.")
        if self.health <= 0:
            return "{self.race} died!"


    
    def describe(self):
        return f"You see a {self.race} that is {self.size} and has {self.strength} strength and is level {self.level} and has {self.health} hp"

    def attack(self, weapon, target):
        print(f"{self.race} attacks {target.race} with {weapon.name}.")

        total_damage = weapon.damage + self.strength

        target.take_damage(total_damage)

        weapon.degrade()

        if target.health <= 0:
            print(f"You killed {target.race}!")
            self.xpgain(2)


class Weapon:
    def __init__(self, name, damage, durability, size, rarity, special):
        self.name = name
        self.damage = damage
        self.durability = durability
        self.size = size
        self.rarity = rarity
        self.special = special


    def degrade(self):
        if self.durability > 0:
            self.durability -= 1
            print(f"{self.name} durability: {self.durability}")
            if self.durability <= 0:
                print(f"{self.name} broke!")




#class 3


class main():
    
    hero = Entity(20, 1, 0, "large", "Hero", 1)
    enemy = Entity(15, 1, 0, "tiny", "Goat", 1)
    kicking_boots = Weapon("Kicking Boots", 15, 10, "10000", "mythical", "roundhouse")
    hooves = Weapon("Hooves", 1, 15, "tiny", "common", "ram")

    print(f"Behold your mighty hero!!! {hero.describe()}")
    print(f"{enemy.describe()}")
   
    enemy.attack(hooves, hero)

    hero.attack(kicking_boots, enemy)



if __name__ == "__main__":
    main()