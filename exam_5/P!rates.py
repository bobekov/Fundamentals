cities = {}

while True:
    command = input().split("||")
    if command[0] == 'Sail':
        break
    city, population, gold = command[0], int(command[1]), int(command[2])

    if city not in cities:
        cities[city] = [population, gold]
    else:
        cities[city][0] += population
        cities[city][1] += gold

while True:
    new_command = input().split("=>")
    if new_command[0] == 'End':
        break
    elif new_command[0] == 'Plunder':
        city, people, gold = new_command[1], int(new_command[2]), int(new_command[3])

        cities[city][0] -= people
        cities[city][1] -= gold

        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")

        if cities[city][0] <= 0 or cities[city][1] <= 0:
            del cities[city]
            print(f"{city} has been wiped off the map!")

    elif new_command[0] == 'Prosper':
        city, gold = new_command[1], int(new_command[2])
        if gold < 0:
            print(f"Gold added cannot be a negative number!")
        else:
            cities[city][1] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {cities[city][1]} gold.")

if len(cities) > 0:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")

    for city, data in cities.items():
        print(f"{city} -> Population: {data[0]} citizens, Gold: {data[1]} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")





