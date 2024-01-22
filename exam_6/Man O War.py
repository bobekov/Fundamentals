def calculate_status(ship):
    sections = list(map(int, ship.split('>')))
    return sum(sections)

pirate_ship = input()
warship = input()
max_health = int(input())

pirate_sections = pirate_ship.split('>')
warship_sections = warship.split('>')

while True:
    command = input()
    if command == 'Retire':
        break

    tokens = command.split()
    action = tokens[0]

    if action == 'Fire':
        index = int(tokens[1])
        damage = int(tokens[2])
        if 0 <= index < len(warship_sections):
            warship_sections[index] = str(int(warship_sections[index]) - damage)
            if int(warship_sections[index]) <= 0:
                print("You won! The enemy ship has sunken.")
                exit()
    elif action == 'Defend':
        start_index = int(tokens[1])
        end_index = int(tokens[2])
        damage = int(tokens[3])
        if 0 <= start_index < len(pirate_sections) and 0 <= end_index < len(pirate_sections):
            for i in range(start_index, end_index + 1):
                pirate_sections[i] = str(int(pirate_sections[i]) - damage)
                if int(pirate_sections[i]) <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit()
    elif action == 'Repair':
        index = int(tokens[1])
        health = int(tokens[2])
        if 0 <= index < len(pirate_sections):
            pirate_sections[index] = str(min(int(pirate_sections[index]) + health, max_health))
    elif action == 'Status':
        count = sum(1 for section in pirate_sections if int(section) < max_health * 0.2)
        print(f"{count} sections need repair.")

pirate_ship_status = calculate_status('>'.join(pirate_sections))
warship_status = calculate_status('>'.join(warship_sections))

print(f"Pirate ship status: {pirate_ship_status}")
print(f"Warship status: {warship_status}")