size = int(input())

mxt = []
alice_pos = []
tea_bags = 0
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
for row in range(size):
    mxt.append(input().split())

    if "A" in mxt[row]:
        alice_pos = [row, mxt[row].index("A")]
        mxt[row][alice_pos[1]] = "*"

while tea_bags < 10:
    direction = input()

    row = alice_pos[0] + directions[direction][0]
    col = alice_pos[1] + directions[direction][1]

    if not (0 <= row < size and 0 <= col < size):
        break

    alice_pos = [row, col]
    pos = mxt[row][col]
    mxt[row][col] = "*"

    if pos == "R":
        break

    if pos.isdigit():
        tea_bags += int(pos)

if tea_bags < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

print(*[" ".join(row) for row in mxt], sep="\n")
