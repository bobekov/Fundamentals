heroes = {}
n = int(input())

for _ in range(n):
    string = input().split()
    name, HP, MP = string[0], int(string[1]), int(string[2])

    if name not in heroes:
        heroes[name] = [HP, MP]

while True:
    command = input().split(" - ")
    if command[0] == 'End':
        break
    elif command[0] == 'CastSpell':
        hero_name, MP_needed, spell_name = command[1], int(command[2]), command[3]

        if heroes[hero_name][1] >= MP_needed:
            heroes[hero_name][1] -= MP_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif command[0] == 'TakeDamage':
        hero_name, damage, attacker = command[1], int(command[2]), command[3]
        heroes[hero_name][0] -= damage

        if heroes[hero_name][0] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name][0]} HP left!")
        else:
            del heroes[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")

    elif command[0] == 'Recharge':
        hero_name, amount = command[1], int(command[2])

        recovered = 200 - heroes[hero_name][1]
        heroes[hero_name][1] += amount
        if heroes[hero_name][1] > 200:
            heroes[hero_name][1] = 200

        print(f"{hero_name} recharged for {amount if heroes[hero_name][1] < 200 else recovered} MP!")

    elif command[0] == 'Heal':
        hero_name, amount = command[1], int(command[2])

        recovered = 100 - heroes[hero_name][0]
        heroes[hero_name][0] += amount
        if heroes[hero_name][0] > 100:
            heroes[hero_name][0] = 100

        print(f"{hero_name} healed for {amount if heroes[hero_name][0] < 100 else recovered} HP!")

for hero, data in heroes.items():
    print(f"{hero}\nHP: {data[0]}\nMP: {data[1]}")

