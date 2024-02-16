def eat_cookie(presents_left, nice_kids):
    for coords in dirs.values():
        r = santa_pos[0] + coords[0]
        c = santa_pos[1] + coords[1]

        if neighbours[r][c].isalpha():
            if neighbours[r][c] == 'V':
                nice_kids += 1

            neighbours[r][c] = '-'
            presents_left -= 1

        if not presents_left:
            break

    return presents_left, nice_kids
presents = int(input())
size = int(input())

neighbours = []
santa_pos = []

total_nice_kids = 0
nice_kids_visited = 0

dirs = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
for r in range(size):
    line = input().split()

    neighbours.append(line)

    if 'S' in line:
        santa_pos = [r, line.index('S')]
        neighbours[r][santa_pos[1]] = '-'

    total_nice_kids += line.count('V')

command = input()

while command != "Christmas morning":
    santa_pos = [
        santa_pos[0] + dirs[command][0],
        santa_pos[1] + dirs[command][1],
    ]

    house = neighbours[santa_pos[0]][santa_pos[1]]

    if house == 'V':
        nice_kids_visited += 1
        presents -= 1
    elif house == 'C':
        presents, nice_kids_visited = eat_cookie(presents, nice_kids_visited)

    neighbours[santa_pos[0]][santa_pos[1]] = '-'

    if not presents or nice_kids_visited == total_nice_kids:
        break

    command = input()
neighbours[santa_pos[0]][santa_pos[1]] = 'S'
if not presents and nice_kids_visited < total_nice_kids:
    print('Santa ran out of presents!')

print(*[' '.join(line) for line in neighbours], sep='\n')

if total_nice_kids == nice_kids_visited:
    print(f'Good job, Santa! {nice_kids_visited} happy nice kid/s.')
else:
    print(f'No presents for {total_nice_kids - nice_kids_visited} nice kid/s.')