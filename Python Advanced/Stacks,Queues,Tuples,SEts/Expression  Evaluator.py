from collections import deque
from math import floor

symbol_nums_list = deque(input().split())
i = 0

while i < len(symbol_nums_list):
    the_element = symbol_nums_list[i]
    if the_element == "-":
        for each in range(i - 1):
            symbol_nums_list.appendleft(
                int(symbol_nums_list.popleft()) - int(symbol_nums_list.popleft())
            )
    elif the_element == "+":
        for each in range(i - 1):
            symbol_nums_list.appendleft(
                int(symbol_nums_list.popleft()) + int(symbol_nums_list.popleft())
            )
    elif the_element == "*":
        for each in range(i - 1):
            symbol_nums_list.appendleft(
                int(symbol_nums_list.popleft()) * int(symbol_nums_list.popleft())
            )
    elif the_element == "/":
        for each in range(i - 1):
            symbol_nums_list.appendleft(
                int(symbol_nums_list.popleft()) / int(symbol_nums_list.popleft())
            )

    if the_element in "*/+-":
        del symbol_nums_list[1]
        i = 1
    i += 1


print(floor(int(symbol_nums_list[0])))
