uinput = input()
position = 0
cur_str = ""
tempstr = ""
numbers = ""


def checkifnum(number):
    if number.isdigit():
        return number


while position < len(uinput):
    if uinput[position].isdigit():
        for eachnum in range(position, len(uinput)):
            if checkifnum(uinput[eachnum]):
                numbers += checkifnum(uinput[eachnum])
            else:
                break
        tempstr += cur_str.upper() * int(numbers)
        numbers = ""
        cur_str = ""
        position += 1
    else:
        cur_str += uinput[position]
        position += 1

unique_symbols_count = len(set(tempstr.upper()))
print(f"Unique symbols used: {unique_symbols_count}")
print(tempstr)
