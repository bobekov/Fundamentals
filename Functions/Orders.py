product = input()
count = float(input())

def order(product):
    sum_price = 0
    if product == 'coffee':
        sum_price = count * 1.50
    elif product == 'coke':
        sum_price = count * 1.40
    elif product == 'water':
        sum_price = count * 1
    elif product == 'snacks':
        sum_price = count * 2
    return "{:.2f}".format(sum_price)

print(order(product))