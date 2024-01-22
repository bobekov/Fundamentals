import re

text = input()
pattern = r'(::[A-Z][a-z]{2,}::|\*\*[A-Z][a-z]{2,}\*\*)'
matched = re.findall(pattern, text)

cool_number = 1
for num in text:
    if num.isdigit():
        cool_number *= int(num)
print(f"Cool threshold: {cool_number}")

print(f"{len(matched)} emojis found in the text. The cool ones are:")

for match in matched:
    word = match[2:-2]
    sum_word = 0
    for i in word:
        i_digit = ord(i)
        sum_word += i_digit
    if sum_word > cool_number:
        print(match)


