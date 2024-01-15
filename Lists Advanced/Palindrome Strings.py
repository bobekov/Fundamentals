def palindrom_filtered(word):
    if word == word[::-1]:
        return word

words = input().split()
palindrome = input()

lst = [word for word in words if palindrom_filtered(word)]

palindrome_counter = lst.count(palindrome)

print(lst)
print(f"Found palindrome {palindrome_counter} times")