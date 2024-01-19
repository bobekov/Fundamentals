FIRST_COUNT = 5

numbers = [int(x) for x in input().split()]
avg_num = sum(numbers) / len(numbers)
filtered_nums = sorted([x for x in numbers if x > avg_num])

if not filtered_nums:
    print("No")
else:
    for i in range(FIRST_COUNT):
        if filtered_nums:
            print(filtered_nums.pop(), end=" ")