rooms = input().split("|")
health = 100
bitcoins = 0
best_room = 0

for room in rooms:
    command, value = room.split()
    value = int(value)
    best_room += 1

    if command == "potion":
        healed_amount = min(value, 100 - health)
        health += healed_amount
        print(f"You healed for {healed_amount} hp.")
        print(f"Current health: {health} hp.")
    elif command == "chest":
        bitcoins += value
        print(f"You found {value} bitcoins.")
    else:
        health -= value
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {best_room}")
            break

if health > 0:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")