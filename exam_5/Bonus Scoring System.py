number_student = int(input())
number_lecture = int(input())
bonus = int(input())
total_bonus = 0
max_bonus = 0
attendances = 0

for student in range(number_student):
    count_attendances = int(input())
    total_bonus = count_attendances / number_lecture * (5 + bonus)

    if total_bonus > max_bonus:
        max_bonus = total_bonus
        attendances = count_attendances

print(f"Max Bonus: {round(max_bonus)}.")
print(f"The student has attended {attendances} lectures.")