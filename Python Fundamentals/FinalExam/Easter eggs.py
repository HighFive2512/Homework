import re


input_str = input()


egg_matches = re.findall(r"[@#]+([a-z]{3,})[@#]+[^A-Za-z0-9]*?/(\d+)/", input_str)

for egg_match in egg_matches:
    color, amount = egg_match[0], egg_match[1]
    if color == color.lower():
        print(f"You found {amount} {color} eggs!")
