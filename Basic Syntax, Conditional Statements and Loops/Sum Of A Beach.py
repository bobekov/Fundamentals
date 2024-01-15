string = input().lower()

counter = 0
words = ["sand", "water", "fish", "sun"]

for i in words:
    counter += string.count(i)

print(counter)