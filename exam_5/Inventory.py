journal = input().split(", ")

while True:
    text = input()
    if text == 'Craft!':
        break
    command = text.split(" - ")
    if command[0] == 'Collect':
        item = command[1]
        if item in journal:
            continue
        else:
            journal.append(item)
    elif command[0] == 'Drop':
        item = command[1]
        if item in journal:
            journal.remove(item)
    elif command[0] == 'Combine Items':
        item = command[1].split(":")
        old_item = item[0]
        new_item = item[1]
        if old_item in journal:
            index = journal.index(old_item)
            journal.insert(index + 1, new_item)
    elif command[0] == 'Renew':
        item = command[1]
        if item in journal:
            journal.remove(item)
            journal.append(item)

print(", ".join(journal))