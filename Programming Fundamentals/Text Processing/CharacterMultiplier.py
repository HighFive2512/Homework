total = 0
uinput = input().split(" ")
firstWord,secondWord = uinput[0],uinput[1]
longerword, shorterword = (firstWord if len(firstWord) > len(secondWord) else secondWord),(firstWord if len(firstWord) < len(secondWord) else secondWord)
for eachchar in range(len(shorterword)):
    total += ord(firstWord[eachchar]) * ord(secondWord[eachchar])
if len(firstWord) != len(secondWord):
    for eachmaxchar in range(len(shorterword),len(longerword)):
        total += ord(longerword[eachmaxchar])
print(total)