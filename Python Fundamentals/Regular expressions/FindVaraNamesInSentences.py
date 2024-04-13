import re

uinput = input()
pattern = r"\b_([A-Za-z0-9]+)\b"
res = re.findall(pattern, uinput)
print(*res, sep=",")
