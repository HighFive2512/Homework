size = int(input())
mxt = [[int(x) for x in input().split()] for _ in range(size)]

cmd = input().split()

while cmd[0] != "END":
    type_command, row, col, value = cmd[0], int(cmd[1]), int(cmd[2]), int(cmd[3])

    if not (0 <= row < size and 0 <= col < size):
        print("Invalid coordinates")
    elif type_command == "Add":
        mxt[row][col] += value
    elif type_command == "Subtract":
        mxt[row][col] -= value
    cmd = input().split()

[print(*r) for r in mxt]
