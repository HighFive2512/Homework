uinput = int(input())

odd, even = set(), set()
for each_input in range(uinput):
    temp_word = input()
    temp_num = 0
    for each_leter in temp_word:
        temp_num += int(ord(each_leter))
    temp_num = temp_num // (int(each_input) + 1)
    if temp_num % 2 == 0:
        even.add(temp_num)
    else:
        odd.add(temp_num)

if sum(odd) == sum(even):
    print(*odd.union(even), sep=", ")
if sum(odd) > sum(even):
    print(*odd.difference(even), sep=", ")
if sum(odd) < sum(even):
    print(*odd.symmetric_difference(even), sep=", ")
