import time


class enemy:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class weapon:
    def __init__(self, name, type, damage, durability):
        self.name = name
        self.type = type
        self.damage = damage
        self.durability = durability
    def attack(self, enemy):
        self.durability -= 1
        print(troll.hp)
        troll.hp = troll.hp - self.damage
        print(troll.hp)
        print(self.damage)
        return (f"{self.name} deals {self.damage} damage and has {self.durability} durability. \n {troll.name} has {troll.hp} hp remaining.")

bow = weapon("Big Bow", "bow", 4, 41)
troll = enemy("Troll", 10)
while troll.hp > 0:
    print(bow.attack(troll))
    time.sleep(1)
print(f"You defeated {troll.name}")


