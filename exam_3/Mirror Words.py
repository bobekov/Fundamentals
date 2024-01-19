import re

text = input()

pattern = r"([@#])([A-Za-z]{3,})(\1)(\1)([A-Za-z]{3,})(\1)"
matched = re.findall(pattern, text)

if len(matched) > 0:
    print(f"{len(matched)} word pairs found!")
else:
    print(f"No word pairs found!")

pairs = []
for match in matched:
    first = match[1]
    second = match[4]
    if first == second[::-1]:
        pairs.append(f"{first} <=> {second}")

if len(pairs) > 0:
    print(f"The mirror words are:")
    print(", ".join(pairs))
else:
    print(f"No mirror words!")
