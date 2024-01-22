quantity_food = float(input())
quantity_hay = float(input())
quantity_cover = float(input())
guinea_weight = float(input())

for day in range(1, 30+1):
    quantity_food -= 0.3
    if day % 2 == 0:
        quantity_hay -= quantity_food * 0.05
    if day % 3 == 0:
        quantity_cover -= guinea_weight / 3

if quantity_food <= 0 or quantity_hay <= 0 or quantity_cover <= 0:
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {quantity_food:.2f},"
          f" Hay: {quantity_hay:.2f}, Cover: {quantity_cover:.2f}.")