from collections import deque

buzzz = deque(int(x) for x in input().split())
nektar = [int(x) for x in input().split()]
symbols = deque(input().split())

result = 0

functions = {
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else 0,
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
}

while buzzz and nektar:
    curr_bee = buzzz.popleft()
    curr_nektar = nektar.pop()

    if curr_nektar < curr_bee:
        buzzz.appendleft(curr_bee)
    else:
        result += abs(functions[symbols.popleft()](curr_bee, curr_nektar))

print(f"Total honey made: {result}")

if buzzz:
    print(f"Bees left: {', '.join(str(x) for x in buzzz)}")

if nektar:
    print(f"nectar left: {', '.join(str(x) for x in nektar)}")
