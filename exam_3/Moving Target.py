targets = list(map(int, input().split()))

while True:
    command = input()
    if command == "End":
        break
    command = command.split()
    action = command[0]

    if action == "Shoot":
        index = int(command[1])
        power = int(command[2])

        if 0 <= index < len(targets):
            targets[index] -= power

            if targets[index] <= 0:
                targets.pop(index)
        else:
            continue

    elif action == "Add":
        index = int(command[1])
        value = int(command[2])

        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
            continue

    elif action == "Strike":
        index = int(command[1])
        radius = int(command[2])
        start_index = index - radius
        end_index = index + radius

        if 0 <= start_index < len(targets) and 0 <= end_index < len(targets):
            targets = targets[:start_index] + targets[end_index+1:]
        else:
            print("Strike missed!")
            continue

print("|".join(map(str, targets)))