mxt = [list(input().strip()) for eachrow in range(int(input()))]

start_pos = None

starting_armour = 300

for each_list in range(len(mxt)):
    current_list = mxt[each_list]
    if 'J' in mxt[each_list]:
        row,col = (each_list, mxt[each_list].index('J'))
        break

while True:
    direction = input()
    mxt[row][col] = "-"
    if direction == "up":
        row -= 1
    if direction == "down":
        row += 1
    if direction == "left":
        col -= 1
    if direction == "right":
        col += 1

    if mxt[row][col] == "E":
        if starting_armour > 100 :
            starting_armour -= 100

        else:
            mxt[row][col] = "J"
            print(f'Mission failed, your jetfighter was shot down! Last coordinates [{row}, {col}]!')
            print('\n'.join(''.join(x) for x in mxt))
            break

    if mxt[row][col] == "R":
        starting_armour = 300
        mxt[row][col] = "-"

    mxt[row][col] = "J"

    found = any("E" in eachlist for eachlist in mxt)
    if found == False:
        print(f'Mission accomplished, you neutralized the aerial threat!')
        print('\n'.join(''.join(x) for x in mxt))
        break
