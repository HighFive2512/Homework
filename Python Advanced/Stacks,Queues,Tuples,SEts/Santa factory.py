from collections import deque

mats = [int(x) for x in input().split()]
magicu = deque(int(x) for x in input().split())

done = []
gifts = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

while mats and magicu:
    mat = mats.pop() if magicu[0] or not mats[-1] else 0  # 0
    mag = magicu.popleft() if mat or not magicu[0] else 0  # 0

    if not mag:
        continue

    product = mat * mag

    if gifts.get(product):
        done.append(gifts[product])
    elif product < 0:
        mats.append(mat + mag)
    elif product > 0:
        mats.append(mat + 15)

if {"Doll", "Wooden train"}.issubset(done) or {"Teddy bear", "Bicycle"}.issubset(done):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if mats:
    print(f"Materials left: {', '.join(str(x) for x in mats[::-1])}")

if magicu:
    print(f"Magic left: {', '.join(str(x) for x in magicu)}")

[print(f"{toy}: {done.count(toy)}") for toy in sorted(set(done))]
