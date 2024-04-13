from math import ceil


def merge(string, parameters):
    param1, param2 = parameters
    param1 = int(param1)
    param2 = int(param2)
    if param1 < 0:
        param1 = 0
    if int(param2) >= len(string):
        param2 = len(string)
    combined = "".join(string[param1 : param2 + 1])
    string[param1 : param2 + 1] = [combined]
    return string


def divide(string, parameters):
    param1, param2 = parameters
    param1 = int(param1)
    param2 = int(param2)
    selected_string = string[param1]
    selected_index = string.index(selected_string)
    tempolist = []
    divide_by = len(selected_string) // param2
    for eachindx in range(param2):
        if eachindx == param2 - 1:
            tempolist.append(selected_string[eachindx * divide_by :])
        else:
            tempolist.append(
                selected_string[eachindx * divide_by : (eachindx + 1) * divide_by]
            )

    string.pop(selected_index)

    for i in range(len(tempolist)):
        string.insert(selected_index + i, tempolist[i])
    return string


fullstring = [x for x in input().split(" ")]
while True:
    command = input()
    if str(command).strip() == "3:1":
        print(*fullstring)
        exit()

    commandparams = [x for x in command.split(" ")]
    if commandparams[0] == "merge":
        commandparams.pop(0)
        fullstring = merge(fullstring, commandparams)
    elif commandparams[0] == "divide":
        commandparams.pop(0)
        fullstring = divide(fullstring, commandparams)
