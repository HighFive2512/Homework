def version_changer(ver):
    flag = "n"
    for n in range(len(ver), -1, -1):
        if n == len(ver) - 1:
            if ver[n] == 9:
                ver[n] = 0
                flag = "y"
            else:
                ver[n] += 1
        elif n == 0:
            if flag == "y":
                ver[n] += 1
        elif flag == "y":
            if ver[n] == 9:
                ver[n] = 0
            else:
                ver[n] += 1
                flag = "n"
    return ver


version = [int(x) for x in input().split(".")]
next_ver = version_changer(version)
print(*next_ver, sep=".")
