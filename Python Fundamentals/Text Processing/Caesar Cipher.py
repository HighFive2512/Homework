encryptedtext = ""
uinput = input()
for eachchar in uinput:
    encryptedtext += chr(ord(eachchar) + 3)
print(encryptedtext)
