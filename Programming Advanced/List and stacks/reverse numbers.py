from collections import deque

reverse_stack = deque()
uinput = [i for i in input().split(" ")]
for eachnum in uinput:
	reverse_stack.append(eachnum)
revnums = []
while reverse_stack:
	revnums.append(reverse_stack.pop())

print(" ".join(map(str,revnums)))