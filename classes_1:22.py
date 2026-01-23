import random

#class 1
class Entity:
    def __init__(self, health, level, xp, size, race, strength):
        self.health = health
        self.level = level
        self.xp = xp
        self.size = size
        self.race = race
        self.strength = strength
   
    def level_up(self):
        requirement = self.level * 2
        while self.xp >= requirement:
            requirement = self.level*2
            self.level += 1
            print("You leveled up!")

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            return "{self.race} died!"
   
    def xpgain(self, mult):
        gain = random.randint(1,5)
        gain = gain * 1.3 * mult
        self.xp += gain
    
    def describe(self):
        return f"You see a {self.race} that is {self.size} and has {self.strength} strength and is level {self.level} and has {self.health} hp"

class Weapon:
    def __init__(self, name, damage, durability, size, rarity, special):
        self.name = name
        self.damage = damage
        self.durability = durability
        self.size = size
        self.rarity = rarity
        self.special = special
    #Things that happen when attack
    
    def attack(self, target):
        target = target.health
        if self.durability > 0:
            target -= self.damage
            self.durability -= 1
            print(f" {self.name} has {self.durability} durability remaining")
            if self.durability <=0:
                return f"{self.name} broke!"
            return target





#class 3


class main():
    
    hero = Entity(20, 1, 0, "large", "You", 1)
    nubian_goat = Entity(15, 1, 0, "tiny", "Goat", 1)
    kicking_boots = Weapon("Kicking Boots", 15, 10, "10000", "mythical", "roundhouse")
    hooves = Weapon("Hooves", 1, 15, "tiny", "common", "ram")

#    print(f"Behold your mighty hero!!! {hero.describe()}")
#    print(f"{nubian_goat.describe()}")

    print(f"Goat uses {hooves.special}")
    hooves.attack(hero)
    
    #print(f"{nubian_goat.race} dealt {tempatt} damage!.")

    #hero.take_damage(tempatt)
    print(f"You now have {hero.health} hp. ")

    print(f"You use with {kicking_boots.special}.")
    tempatt = kicking_boots.attack(nubian_goat)
    print(f"You dealt {tempatt} damage!")

    nubian_goat.take_damage(tempatt)
    print(f"{nubian_goat.race} now has {nubian_goat.health} hp")

    if nubian_goat.health <= 0:
        hero.xpgain(1)
        hero.level_up()
        print(hero.xp)
        print(hero.level)
        print(f"You are now level {hero.level}")
        


if __name__ == "__main__":
    main()