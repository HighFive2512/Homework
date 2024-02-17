import re

user_string = input()
pattern = r'\s(([A-Za-z0-9]+[A-Za-z0-9\_\.\-]*)@([a-z\-]+)(\.[a-z]+)+)\b'
res = re.findall(pattern,user_string)
for each in res:
    print(each[0])