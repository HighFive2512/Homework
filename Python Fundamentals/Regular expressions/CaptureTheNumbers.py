import re

userinput = input()
while userinput:
    res = re.findall(r"\d+", userinput)
    if res:
        print(" ".join(res), end=" ")
    userinput = input()
