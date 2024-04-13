import re


sentence_uinput = input()
keyword_to_look_for = input().strip()
pattern = rf"\b{re.escape(keyword_to_look_for)}\b"
print(len(re.findall(pattern, sentence_uinput, re.IGNORECASE)))
