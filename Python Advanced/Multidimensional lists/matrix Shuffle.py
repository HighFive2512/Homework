def check_indices_valid(indc):
    return {indc[0], indc[2]}.issubset(valid_rows) and {indc[1], indc[3]}.issubset(
        valid_cols
    )


def swap_elements(command, indices):
    if len(indices) == 4 and check_indices_valid(indices) and command == "swap":
        row1, col1, row2, col2 = indices
        mx[row1][col1], mx[row2][col2] = mx[row2][col2], mx[row1][col1]

        [print(*row) for row in mx]
    else:
        print("Invalid input!")


rows, cols = [int(x) for x in input().split()]
mx = [input().split() for _ in range(rows)]

valid_rows = range(rows)
valid_cols = range(cols)

while True:
    cmds, *coords = [int(x) if x.isdigit() else x for x in input().split()]

    if cmds == "END":
        break

    swap_elements(cmds, coords)
