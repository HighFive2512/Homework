uinput = input()
filtered_output = ""
for eachchar in range(len(uinput)):
    if eachchar == 0:
        filtered_output += uinput[eachchar]
    else:
        if eachchar >= len(uinput):
            break
        else:
            if uinput[eachchar] != uinput[eachchar - 1]:
                filtered_output += uinput[eachchar]
print(filtered_output)
