def shells_filler(shells):
    num = 1
    shell_list = []
    while True:
        filledshell = 2*(num**2)
        if shells >= filledshell:
            shell_list.append(filledshell)
            shells -= filledshell
        else:
            shell_list.append(shells)
            break
        num += 1
    return shell_list

inp_shells = int(input())
result = shells_filler(inp_shells)
print(result)
