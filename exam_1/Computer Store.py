total_price_without_taxes = 0
total_amount_of_taxes = 0
special_custom = False

while True:
    command = input()
    if command == 'special':
        special_custom = True
        break
    if command == 'regular':
        break
    price = float(command)
    if price <= 0:
        print("Invalid price!")
    else:
        total_price_without_taxes += price
        total_amount_of_taxes += price * 0.2

final_price = total_price_without_taxes + total_amount_of_taxes

if special_custom:
    final_price -= final_price * 0.1

if final_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price_without_taxes:.2f}$")
    print(f"Taxes: {total_amount_of_taxes:.2f}$")
    print("-----------")
    print(f"Total price: {final_price:.2f}$")

