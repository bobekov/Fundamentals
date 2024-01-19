sentence = input()

while True:
    command = input().strip().split(":")
    if command[0] == 'Travel':
        break
    elif command[0] == 'Add Stop':
        index, string = int(command[1]), command[2]
        if 0 <= index <= len(sentence):
            sentence = sentence[:index] + string + sentence[index:]
        print(sentence)

    elif command[0] == 'Remove Stop':
        start_index, end_index = int(command[1]), int(command[2])
        if 0 <= start_index <= end_index < len(sentence):
            sentence = sentence[:start_index] + sentence[end_index+1:]
        print(sentence)

    elif command[0] == 'Switch':
        old_string, new_string = command[1], command[2]
        if old_string in sentence:
            sentence = sentence.replace(old_string, new_string)
        print(sentence)

print(f"Ready for world tour! Planned stops: {sentence}")