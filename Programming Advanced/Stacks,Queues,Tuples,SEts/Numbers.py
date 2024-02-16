First,Second = set(int(x) for x in input().split(" ")),set(int(x) for x in input().split(" "))

for each_opertaion in range(int(input())):
    uinput = input().split(" ")
    tar_var = globals().get(uinput[1])
    if uinput[0] == "Add":
        for eachnum in uinput[2:]:
            if int(eachnum) not in tar_var:
                tar_var.add(int(eachnum))
    if uinput[0] == "Remove":
        for eachnum in uinput[2:]:
            if int(eachnum) in tar_var:
                tar_var.remove(int(eachnum))
    if uinput[0] == "Check":
        print(Second <= First)
print(*sorted(First),sep=", ")
print(*sorted(Second),sep=", ")