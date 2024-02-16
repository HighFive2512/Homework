n = int(input())

matrica = [[int(el) for el in input().split(", ")] for _ in range(n)]
main_one = [matrica[r][r] for r in range(n)]
secondary_one = [matrica[r][n - r - 1] for r in range(n)]

print(f"Primary diagonal: {', '.join(str(x) for x in main_one)}. Sum: {sum(main_one)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_one)}. Sum: {sum(secondary_one)}")