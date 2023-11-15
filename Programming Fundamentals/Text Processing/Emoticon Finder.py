uinput = input()
indexes = [indx for indx,char in enumerate(uinput) if char == ":"]
for eachindx in indexes:
    if uinput[eachindx+1] != " ":
        print(uinput[eachindx]+uinput[eachindx+1])