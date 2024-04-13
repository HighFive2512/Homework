result = set()

for each_intersection in range(int(input())):
    comma_entry = input().split("-")

    firstnum, secondnum = comma_entry[0].split(","), comma_entry[1].split(",")
    set1, set2 = set(range(int(firstnum[0]), int(firstnum[1]) + 1)), set(
        range(int(secondnum[0]), int(secondnum[1]) + 1)
    )
    temp_intersection = set1.intersection(set2)
    if len(temp_intersection) > len(result):
        result = list(temp_intersection.copy())

print(f"Longest intersection is {result} with length {len(result)}")
