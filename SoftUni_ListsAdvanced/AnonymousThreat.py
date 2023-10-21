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
def divide(string,parameters):
    param1, param2 = parameters
    param1 = int(param1)
    param2 = int(param2)
    while True:
        selected_string = string[param1]
        tempolist = []
        selected_index = string.index(selected_string)
        previndex = 0
        divide_by = len(string) // param2
        for each_index in range(2,len(selected_string),1+divide_by):
            if each_index+1 == param2+1:
                if len(selected_string) % 2 == 1:
                    tempolist[previndex] = selected_string[previndex:each_index+1]
                else:
                    tempolist[-1] = selected_string[previndex:each_index]
            tempolist.append(selected_string[previndex:each_index])
            previndex = each_index
        break
    string.pop(selected_index)
    for i in range(len(tempolist)):
        string.insert(selected_index+i,tempolist[i])
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