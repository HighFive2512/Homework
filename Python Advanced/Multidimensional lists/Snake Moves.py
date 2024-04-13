from collections import deque

r, c = [int(x) for x in input().split()]
word = list(input())

word_copy = deque(word)
multi = 1

for row in range(r):
    while len(word_copy) < c:
        word_copy.extend(word)

    print(*[word_copy.popleft() for _ in range(c)][::multi], sep="")
    multi *= -1
