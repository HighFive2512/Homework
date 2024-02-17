regplates = {}
amountofinputs = int(input())
for eachinput in range(amountofinputs):
    uinput = input().split(" ")
    regtype, usrname = uinput[0],uinput[1]
    if regtype == 'register':
        lplate = uinput[2]
        if usrname in regplates:
            print(f'ERROR: already registered with plate number {lplate}')
        else:
            print(f"{usrname} registered {lplate} successfully")
            regplates[usrname] = lplate
    elif regtype == 'unregister':
        if usrname in regplates:
            print(f"{usrname} unregistered successfully")
            regplates.pop(usrname)
        else:
            print(f"ERROR: user {usrname} not found")
res = [print(f'{usr} => {plate}') for usr, plate in regplates.items()]