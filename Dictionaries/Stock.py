elements = input().split()
data = {}

for i in range(0, len(elements), 2):
    product = elements[i]
    quantity = int(elements[i + 1])
    data[product] = quantity

search_product = input().split()

for product in search_product:
    if product in data:
        print(f"We have {data[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")