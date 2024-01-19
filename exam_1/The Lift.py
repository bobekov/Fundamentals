MAX_SIZE = 4
people = int(input())
lift = [int(x) for x in input().split()]

for i in range(len(lift)):
    free_spaces = MAX_SIZE - lift[i]

    if people >= free_spaces:
        lift[i] += free_spaces
    else:
        lift[i] += people

    people -= free_spaces

    if people <= 0 and (i != len(lift) - 1 or lift[i] < MAX_SIZE):
        print("The lift has empty spots!")
        break
else:
    if people > 0:
        print(f"There isn't enough space! {people} people in a queue!")

print(*lift)