phonedict = {}
while True:
    uinput = input()
    if uinput.isdigit():
        break
    else:
        uinput = uinput.split("-")
        phonedict[uinput[0]] = uinput[1]


for each in range(int(uinput)):
    uinput2 = input()
    if uinput2 in phonedict:
        print(f"{uinput2} -> {phonedict[uinput2]}")
    else:
        print(f"Contact {uinput2} does not exist.")