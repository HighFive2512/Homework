LegmMats = {"shards": 0, "fragments": 0, "motes": 0}
junkmats = {}
startindx = 0
MatsPrompt = input().split()
obtained = False
while True:
    mats = MatsPrompt[startindx + 1].lower()
    matsamount = int(MatsPrompt[startindx])
    if MatsPrompt[startindx + 1].lower() in ["shards", "motes", "fragments"]:
        if mats not in LegmMats:
            LegmMats[mats] = matsamount
        else:
            LegmMats[mats] += matsamount
            if LegmMats[mats] >= 250:
                LegmMats[mats] = LegmMats[mats] - 250
                if mats == "motes":
                    print("Dragonwrath obtained!")
                    obtained = True
                    break
                elif mats == "shards":
                    print("Shadowmourne obtained!")
                    obtained = True
                    break
                elif mats == "fragments":
                    print("Valanyr obtained!")
                    obtained = True
                    break
    else:
        if mats not in junkmats:
            junkmats[mats] = matsamount
        else:
            junkmats[mats] += matsamount

    if startindx + 2 < len(MatsPrompt):
        startindx += 2
        if obtained:
            break
    else:
        MatsPrompt = input().split()
        startindx = 0
    if len(MatsPrompt) == 0:
        break

[print(f"{k}: {v}") for k, v in LegmMats.items()]
[print(f"{k}: {v}") for k, v in junkmats.items()]
