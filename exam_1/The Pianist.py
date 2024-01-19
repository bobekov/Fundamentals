pianists = {}
n = int(input())

for _ in range(n):
    string = input().split("|")
    piece, composer, key = string[0], string[1], string[2]
    if piece not in pianists:
        pianists[piece] = [composer, key]

while True:
    command = input().split("|")
    if command[0] == 'Stop':
        break
    elif command[0] == 'Add':
        piece, composer, key = command[1], command[2], command[3]
        if piece not in pianists:
            pianists[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif command[0] == 'Remove':
        piece = command[1]
        if piece in pianists:
            del pianists[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif command[0] == 'ChangeKey':
        piece, new_key = command[1], command[2]
        if piece in pianists:
            pianists[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for piece, data in pianists.items():
    print(f"{piece} -> Composer: {data[0]}, Key: {data[1]}")

