text = input()
filtered = [letter for letter in text if letter.lower() not in['a', 'o', 'u', 'e', 'i']]

print("".join(filtered))