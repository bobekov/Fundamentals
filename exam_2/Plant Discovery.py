plants = {}
n = int(input())

for _ in range(n):
    command = input().split("<->")
    plant, rarity = command[0], int(command[1])
    if plant not in plants:
        plants[plant] = {'Rarity': rarity, 'Rating': []}

while True:
    commands = input().split(": ")
    if commands[0] == 'Exhibition':
        break
    data = commands[1].split(" - ")
    if data[0] not in plants:
        print('error')

    elif commands[0] == 'Rate':
        plant, rating = data[0], int(data[1])
        plants[plant]['Rating'].append(rating)

    elif commands[0] == 'Update':
        plant, new_rarity = data[0], int(data[1])
        plants[plant]['Rarity'] = new_rarity

    elif commands[0] == 'Reset':
        plant = data[0]
        plants[plant]['Rating'].clear()

print("Plants for the exhibition:")
for plant, data in plants.items():
    average_rating = sum(data['Rating'])
    if len(data['Rating']) > 1:
        average_rating = average_rating / len(data['Rating'])

    print(f"- {plant}; Rarity: {data['Rarity']}; Rating: {average_rating:.2f}")