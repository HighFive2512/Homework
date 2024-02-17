r, c = [int(el) for el in input().split()]
matrix = [input().split() for _ in range(r)]

res = 0

for row in range(r - 1):
    for col in range(c - 1):
        symbol = matrix[row][col]

        if symbol == matrix[row + 1][col] and symbol == matrix[row][col + 1] and symbol == matrix[row + 1][col + 1]:
            res += 1

print(res)