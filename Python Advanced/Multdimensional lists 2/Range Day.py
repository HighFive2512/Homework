def move(direction, steps):
    r = my_pos[0] + (directs[direction][0] * steps)
    c = my_pos[1] + (directs[direction][1] * steps)

    if not (0 <= r < SIZE and 0 <= c < SIZE):
        return my_pos
    if field[r][c] == "x":
        return my_pos

    return [r, c]


def shoot(direction):
    r = my_pos[0] + directs[direction][0]
    c = my_pos[1] + directs[direction][1]

    while 0 <= r < SIZE and 0 <= c < SIZE:
        if field[r][c] == "x":
            field[r][c] = "."
            return [r, c]

        r += directs[direction][0]
        c += directs[direction][1]


SIZE = 5
field = []

tars = 0
tar = 0
targets_hit_positions = []

my_pos = []

directs = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(SIZE):
    field.append(input().split())

    if "A" in field[row]:
        my_pos = [row, field[row].index("A")]

    tars += field[row].count("x")

for _ in range(int(input())):
    command_info = input().split()

    if command_info[0] == "move":
        my_pos = move(command_info[1], int(command_info[2]))
    elif command_info[0] == "shoot":
        target_down_pos = shoot(command_info[1])

        if target_down_pos:
            targets_hit_positions.append(target_down_pos)
            tar += 1

        if tar == tars:
            print(f"Training completed! All {tars} targets hit.")
            break

if tar < tars:
    print(f"Training not completed! {tars - tar} targets left.")

print(*targets_hit_positions, sep="\n")
