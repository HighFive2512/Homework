username = list()

uinput = int(input())

for eachinput in range(uinput):
    check_name = input()
    if check_name not in username:
        username.append(check_name)

for eachentry in username:
    print(eachentry)