from collections import deque

stacked_query = []
res = []

iterations = int(input())
for eachiter in range(iterations):
    uinput = input().split(" ")
    command = int(uinput[0])
    if command == 1:
        stacked_query.append(int(uinput[1]))
    elif command == 2:
        if stacked_query:
            stacked_query.pop()
    elif command == 3:
        print(max(stacked_query))
    elif command == 4:
        print(min(stacked_query))

while stacked_query:
    res.append(stacked_query.pop())
print(*res,sep=", ")