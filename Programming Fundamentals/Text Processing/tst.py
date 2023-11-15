uinput = input()
result = ""
current_indx = 0
prev_explode = 0

while current_indx < len(uinput):
    if uinput[current_indx] == ">":
        if current_indx + 1 < len(uinput):  # Check if there's a character after ">"
            if uinput[current_indx - 2] == ">" and uinput[current_indx + 1].isdigit():
                prev_explode = int(uinput[current_indx + 1])
            else:
                result += uinput[current_indx]
                current_indx += 1
        else:
            break
    else:
        if uinput[current_indx - 2] == ">":
            current_indx += prev_explode
        result += uinput[current_indx]
        current_indx += 1

print(result)
