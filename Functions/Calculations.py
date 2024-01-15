operator = input()
first_num = int(input())
second_num = int(input())

def calculate(operator, first_num, second_num):
    if operator == 'multiply':
        return first_num * second_num
    elif operator == 'divide':
        return first_num // second_num
    elif operator == 'add':
        return first_num + second_num
    elif operator == 'subtract':
        return first_num - second_num

print(calculate(operator, first_num, second_num))