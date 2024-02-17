adict = {}
while True:
    uinput1 = input()
    if uinput1 == "stop":
        [print(f"{key} -> {value}") for key,value in adict.items()]
        break
    uinput2 = input()
    if uinput1 not in adict:
        adict[uinput1] = int(uinput2)
    else:
        adict[uinput1] += int(uinput2)