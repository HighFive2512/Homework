r, c = [int(x) for x in input().split()]

start = ord("a")

for row in range(start, start + r):
    for col in range(row, row + c):
        print(chr(row), chr(col), chr(row), sep="", end=" ")

    print()
