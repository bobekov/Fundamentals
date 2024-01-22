initial_list = input().split("!")

while True:
    string = input()
    if string == 'Go Shopping!':
        break
    command = string.split()
    item = command[1]
    if command[0] == 'Urgent':
        if item not in initial_list:
            initial_list.insert(0, item)
    elif command[0] == 'Unnecessary':
        if item in initial_list:
            initial_list.remove(item)
    elif command[0] == 'Correct':
        old_item = command[1]
        new_item = command[2]
        if old_item in initial_list:
            index = initial_list.index(old_item)
            initial_list.remove(old_item)
            initial_list.insert(index, new_item)
    elif command[0] == 'Rearrange':
        if item in initial_list:
            initial_list.remove(item)
            initial_list.append(item)

print(", ".join(initial_list))