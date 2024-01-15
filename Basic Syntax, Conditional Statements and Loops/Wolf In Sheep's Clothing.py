lst = input().split(", ")
lst_reverse = lst[::-1]

for index, animal in enumerate(lst_reverse):
    if animal == 'wolf' and index == 0:
        print('Please go away and stop eating my sheep')
    elif animal == 'wolf':
        print(f'Oi! Sheep number {index}! You are about to be eaten by a wolf!')