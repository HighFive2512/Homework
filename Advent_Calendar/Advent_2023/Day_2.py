import re

maximum_allowed = {"red": 12, "green": 13, "blue": 14}
accepted_entries = 0
minimum_set_of_cubes = 0
while True:

    fewest_number_of_cubes = {"red": 0, "green": 0, "blue": 0}
    uinput = input()
    if uinput == "":
        break
    game_number = re.findall(r"^Game\s(\d+):", uinput)
    game_number = int(game_number[0])
    cube_sets = re.findall(r"^Game\s\d+: (.*)", uinput)
    cube_sets = cube_sets[0].split("; ")
    flag = "N"
    for eachset in cube_sets:
        eachentry = eachset.split(", ")
        for eachsubset in eachentry:
            num, col = eachsubset.split(" ")
            if int(num) > maximum_allowed[col]:
                flag = "Y"
            if int(num) > fewest_number_of_cubes[col]:
                fewest_number_of_cubes[col] = int(num)
    minimum_set_of_cubes += (
        fewest_number_of_cubes["red"]
        * fewest_number_of_cubes["green"]
        * fewest_number_of_cubes["blue"]
    )
    if flag == "N":
        accepted_entries += game_number

print(accepted_entries)
print(minimum_set_of_cubes)
