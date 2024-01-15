string_list = input().split(", ")

sorted_list = sorted(string_list, key=lambda x: (-len(x), x))

print(sorted_list)