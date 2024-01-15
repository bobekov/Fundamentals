numbers = input().split(', ')
non_zero = []
zero = []

for num in numbers:
    if int(num) == 0:
        zero.append(int(num))
    else:
        non_zero.append(int(num))

print(non_zero + zero)