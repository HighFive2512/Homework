uinput = input()
expl_amount = 0
eachchar = 0
result = ""
while eachchar in range(len(uinput)):
    currentchar = uinput[eachchar]
    if expl_amount > 0 and currentchar != ">":
        expl_amount -= 1
        eachchar+=1
    elif currentchar == ">":
        expl_amount += int(uinput[eachchar+1])
        result += currentchar
        eachchar+=1
    else:
        result += currentchar
        eachchar+=1
print(result)