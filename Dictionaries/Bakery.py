elements = input().split()

stock = {}

for i in range(0, len(elements), 2):
    product = elements[i]
    quantity = int(elements[i + 1])
    stock[product] = quantity

print(stock)