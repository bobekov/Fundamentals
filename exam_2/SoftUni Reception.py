employee_efficiency1 = int(input())
employee_efficiency2 = int(input())
employee_efficiency3 = int(input())
students_count = int(input())

student_per_hour = employee_efficiency1 + employee_efficiency2 + employee_efficiency3
time = 0

while students_count > 0:
    students_count -= student_per_hour
    time += 1

    if time % 4 == 0:
        time += 1

print(f"Time needed: {time}h.")