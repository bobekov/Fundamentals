password = input()

while True:
    string = input().split()
    if string[0] == 'Done':
        break
    elif string[0] == 'TakeOdd':
        password = password[1::2]
        print(password)

    elif string[0] == 'Cut':
        index = int(string[1])
        length = int(string[2])
        cut_string = password[index:(index + length)]
        password = password.replace(cut_string, "", 1)
        print(password)

    elif string[0] == 'Substitute':
        substring = string[1]
        substitute = string[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

print(f"Your password is: {password}")