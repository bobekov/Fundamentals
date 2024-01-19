targets = list(map(int, input().split()))

while True:
    command = input()
    if command == "End":
        break
    index = int(command)
    if 0 <= index < len(targets) and targets[index] != -1:
        shot_target = targets[index]
        targets[index] = -1

        for i in range(len(targets)):
            if targets[i] > shot_target:
                targets[i] -= shot_target
            elif targets[i] <= shot_target and targets[i] != -1:
                targets[i] += shot_target

shot_targets = [target for target in targets if target == -1]
print(f"Shot targets: {len(shot_targets)} -> {' '.join(map(str, targets))}")