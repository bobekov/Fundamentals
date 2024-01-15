budget = int(input())

while budget >= 0:
    command = input()
    if command == 'End':
        break
    price = int(command)
    budget -= price

if budget >= 0:
    print('You bought everything needed.')
else:
    print('You went in overdraft!')