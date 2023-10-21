def merge(string,parameters):
    param1, param2 = parameters
    param1 = int(param1)
    param2 = int(param2)
    if int(param2) > len(string):
        param2 = len(string)
        if param1 == param2:
            return string
    combined = string[param1:param2]
    combined = ''.join(combined)
    asd = string[0:param1] + [combined] + string[param2:]
    return asd


def divide(string, parameters):
    param1, param2 = parameters
    param1 = int(param1)
    param2 = int(param2)

    # Check if param1 and param2 are valid indices
    if param1 >= len(string) or param2 >= len(string):
        return string

    selected_string = string[param1]
    tempolist = []
    divide_by = len(selected_string) // param2

    for each_index in range(0, len(selected_string), divide_by):
        tempolist.append(selected_string[each_index:each_index + divide_by])

    # Remove the selected string
    string.pop(param1)

    # Insert the divided parts back into the list
    for i in range(len(tempolist)):
        string.insert(param1 + i, tempolist[i])

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
        fullstring = merge(fullstring,commandparams)
    elif commandparams[0] == "divide":
        commandparams.pop(0)
        fullstring = divide(fullstring,commandparams)