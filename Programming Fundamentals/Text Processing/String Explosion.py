uinput = input()
result = ""
current_indx = 0
xplode = 0
while current_indx in range(len(uinput)):

    if uinput[current_indx] == ">":
        xplode = int(uinput[current_indx+1])
    else:
        result += uinput[current_indx]
        current_indx += 2
    else:
        if current_indx + 1 > len(uinput):
            break
        print(current_indx+1)
        if uinput[current_indx +1] != ">":
            current_indx += xplode
        result += uinput[current_indx]
        current_indx += 1
print(result)