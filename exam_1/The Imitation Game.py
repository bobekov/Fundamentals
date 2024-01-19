message = input()

while True:
    command = input().split("|")
    if command[0] == 'Decode':
        break
    if command[0] == 'Move':
        number_letter = int(command[1])
        message = message[number_letter:] + message[:number_letter]
    elif command[0] == 'Insert':
        index = int(command[1])
        value = command[2]
        message = message[:index] + value + message[index:]
    elif command[0] == 'ChangeAll':
        substring = command[1]
        replacement = command[2]
        message = message.replace(substring, replacement)

print(f"The decrypted message is: {message}")