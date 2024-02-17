forceDict = {}
while True:
    uinput = input()
    if uinput.strip() == "Lumpawaroo":
        break
    if "|" in uinput:
        uinput = uinput.split(" | ")
        forceusr,forceside = uinput[1], uinput[0]
        if forceusr not in forceDict:
            forceDict[forceusr] = forceside
    if "->" in uinput:
        uinput = uinput.split(" -> ")
        forceusr,forceside = uinput[0], uinput[1]
        if forceusr in forceDict:
            forceDict.pop(forceusr)
        forceDict[forceusr] = forceside
        print(f'{forceusr} joins the {forceside} side!')

res = {value: [k for k, v in forceDict.items() if v == value] for value in forceDict.values()}
for eachside,mems in res.items():
    print(f'Side: {eachside}, Members: {len(mems)}')
    [print(f'! {mem}') for mem in mems]
