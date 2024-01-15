n = int(input())
word = input()
strings = []

for _ in range(n):
    string = input()
    strings.append(string)

print(strings)

filter_strings = []

for string in strings:
    if word in string:
        filter_strings.append(string)

print(filter_strings)