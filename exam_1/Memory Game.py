elements = input().split()
moves = 0

while True:
    command = input().split()
    if len(elements) == 0:
        print(f"You have won in {moves} turns!")
        break
    if command[0] == 'end':
        break
    moves += 1
    index1 = int(command[0])
    index2 = int(command[1])
    if index1 == index2 or index1 < 0 or index1 > len(elements) or index2 < 0 or index2 > len(elements):
        middle_of_elements = len(elements) // 2
        elements.insert(middle_of_elements, f"-{moves}a")
        elements.insert(middle_of_elements, f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")
    else:
        if elements[index1] == elements[index2]:
            remove_element = elements[index1]
            elements = [element for element in elements if element != remove_element]
            print(f"Congrats! You have found matching elements - {remove_element}!")
        else:
            print("Try again!")

if len(elements) != 0:
    print(f"Sorry you lose :(\n{' '.join(elements)}")