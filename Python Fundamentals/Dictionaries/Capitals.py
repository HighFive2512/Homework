Capitals = {}
uinput1 = input().split(", ")
uinput2 = input().split(", ")
res = {uinput1[indx]: uinput2[indx] for indx in range(len(uinput1))}
for key, value in res.items():
    print(f"{key} -> {value}")
