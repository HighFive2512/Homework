ele_set = set()

for _ in range(int(input())):
    for each_element in input().split():
        ele_set.add(each_element)

print(*ele_set,sep="\n")