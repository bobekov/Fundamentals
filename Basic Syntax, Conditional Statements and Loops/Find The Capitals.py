text = input()
lst = []

for i in range(len(text)):
    if text[i].isupper():
        lst.append(i)

print(lst)