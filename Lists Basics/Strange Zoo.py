list = []

for _ in range(3):
    data = input()
    list.append(data)

list[0], list[2] = list[2], list[0]
print(list)