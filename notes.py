limit = 41
Inventory = [["Sword", 12, 20],
            ["Atomic Bomb", 1000, 10000000]]
def checkweight():
    weight = 0
    print("Inventory:")
    for list in Inventory:
        weight += list[1]
        print(f" - {list[0]}: {list[1]} kgs, {list[2]} damage")
    print(f"Total weight: {weight} kgs")
    return weight
        

weight = checkweight()

while weight > limit:
    print(f"You have exceeded your {limit} kg weight limit!")
    choice = input(f"What item would you like to drop? ").strip().title()
    for list in Inventory:
        if choice == list[0]:
            Inventory.remove(list)
            print(f"You dropped {choice}.")
            weight = checkweight()
            

        

