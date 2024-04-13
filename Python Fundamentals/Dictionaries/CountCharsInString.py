class CharCountInStr:
    chardict = {}

    def countchars(self, uinput):
        ccount = 0
        uinput = [x for x in uinput]
        while len(uinput) > ccount:
            if uinput[ccount] != " ":
                if uinput[ccount] not in CharCountInStr.chardict:
                    CharCountInStr.chardict[uinput[ccount]] = 1
                else:
                    CharCountInStr.chardict[uinput[ccount]] += 1
            ccount += 1
        for char, val in CharCountInStr.chardict.items():
            print(f"{char} -> {val}")


InputStr = input()
CharCountInStr().countchars(InputStr)
