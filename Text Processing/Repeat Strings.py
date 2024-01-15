strings = input().split()

new_string = [word * len(word) for word in strings]

print("".join(new_string))