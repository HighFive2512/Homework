from collections import deque

chocos = [int(x) for x in input().split(", ")]
cups = deque(int(x) for x in input().split(", "))

shakes = 0

while shakes != 5 and chocos and cups:
    choco = chocos.pop()
    cup = cups.popleft()

    if choco <= 0 and cup <= 0:
        continue
    elif choco <= 0:
        cups.appendleft(cup)
        continue
    elif cup <= 0:
        chocos.append(choco)
        continue

    if cup == choco:
        shakes += 1
    else:
        cups.append(cup)
        chocos.append(choco - 5)
if shakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(x) for x in chocos) or 'empty'}")
print(f"Milk: {', '.join(str(x) for x in cups) or 'empty'}")
