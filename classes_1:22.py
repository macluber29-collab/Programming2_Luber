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
        requirement += (self.level * 2)
        if self.xp >= requirement:
            self.level += 1
    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            return "{self.race} died!"
    def describe(self):
        return f"You see a {self.race} that is {self.size} and has {self.strength} strength and is level {self.level} and has {self.health} hp"

class Weapon:
    def __init__(self, damage, durability, size, rarity, special):
        self.damage = damage
        self.durability = durability
        self.size = size
        self.rarity = rarity
        self.special = special
    #Things that happen when attack
    def attack(self):
        if self.durability > 0:
            self.durability -= 1
            if self.durability <=0:
                return "Weapon broke!"
            return self.damage
    def xpgain(self, enl):
        num = random.randint(1,5)




#class 3


class main():
    
    hero = Entity(20, 1, 0, "large", "Human", 1)
    nubian_goat = Entity(15, 1, 0, "tiny", "Goat", 1)
    kicking_boots = Weapon(15, 10, "10000", "mythical", "roundhouse")
    hooves = Weapon(1, 15, "tiny", "common", "ram")
#    print(f"Behold your mighty hero!!! {hero.describe()}")
#    print(f"{nubian_goat.describe()}")
    print(f"Goat uses with {hooves.special}")
    tempatt = hooves.attack()
    print(f"{nubian_goat.race} dealt {tempatt} damage!.")
    hero.take_damage(tempatt)
    print(f"You now have {hero.health} hp. ")
    print(f"You use with {kicking_boots.special}.")
    tempatt = kicking_boots.attack()
    print(f"You dealt {tempatt} damage!")
    nubian_goat.take_damage(tempatt)
    print(f"{nubian_goat.race} now has {nubian_goat.health} hp")


if __name__ == "__main__":
    main()