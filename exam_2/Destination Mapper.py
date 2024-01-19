import re

text = input()
pattern = r"(=|\/)([A-Z][a-zA-Z]+)\1"
matched = re.findall(pattern, text)

destinations = []
travel_point = 0

for word in matched:
    destination = word[1]
    if len(destination) >= 3:
        destinations.append(destination)
        travel_point += len(destination)

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_point}")