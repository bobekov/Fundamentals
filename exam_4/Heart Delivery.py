houses = list(map(int, input().split("@")))
last_position = 0

while True:
    string = input()
    if string == "Love!":
        break

    command = string.split()
    jump_length = int(command[1])

    if jump_length + last_position >= len(houses):
        last_position = 0
    else:
        last_position = (last_position + jump_length)
    current_house = houses[last_position]

    if current_house == 0:
        print(f"Place {last_position} already had Valentine's day.")
    else:
        current_house -= 2
        houses[last_position] = current_house

        if current_house == 0:
            print(f"Place {last_position} has Valentine's day.")

houses_without_valentine = 0
for house in houses:
    if house > 0:
        houses_without_valentine += 1

print(f"Cupid's last position was {last_position}.")
if sum(houses) == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {houses_without_valentine} places.")