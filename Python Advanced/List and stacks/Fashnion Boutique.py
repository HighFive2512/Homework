nracks = 0
box_of_clothes = [int(i) for i in input().split(" ")]
capacity = int(input())

current_cloth_value = 0
cloth_num = 0
while box_of_clothes:
    current_cloth_value += int(box_of_clothes[-1])
    if current_cloth_value > capacity:
        nracks += 1
        current_cloth_value = int(box_of_clothes[-1])
    elif current_cloth_value == capacity:
        nracks += 1
        current_cloth_value = 0
    cloth_num += 1
    box_of_clothes.pop(-1)


if current_cloth_value > 0:
    nracks += 1

print(nracks)
