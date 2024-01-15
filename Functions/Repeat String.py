string = input()
n = int(input())

new_string = lambda string, n: string * n

print(new_string(string, n))