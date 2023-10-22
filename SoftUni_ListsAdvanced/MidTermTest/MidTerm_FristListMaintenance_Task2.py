
friend_list = {"friends": input().split(", ")}
friend_list["blacklisted"],friend_list["lost"] = [],[]
lost_names = 0
blacklisted_names = 0

while True:

    uinput = input()
    if uinput == "Report":
        print(f'Blacklisted names: {blacklisted_names}')
        print(f'Lost names: {lost_names}')
        print(*friend_list["friends"])
        break

    if "Blacklist" in uinput:
        param = uinput.split(" ")[1]
        if param in friend_list["friends"]:
            param_loc = friend_list["friends"].index(param)
            friend_list["blacklisted"].append(param)
            blacklisted_names += 1
            friend_list["friends"][param_loc] = "Blacklisted"
            print(f'{param} was blacklisted.')
        else:
            print(f'{param} was not found.')
    if "Error" in uinput:
        param = uinput.split(" ")[1]
        param = int(param)
        if param < len(friend_list["friends"]) and param >= 0:
            currentname = friend_list["friends"][param]
            if currentname == "Blacklisted" or currentname == "Lost":
                ...
            else:
                friend_list["lost"].append(currentname)
                lost_names +=1
                print(f'{currentname} was lost due to an error.')
                friend_list["friends"][param] = "Lost"

    if "Change" in uinput:
        param,param1,param2 = uinput.split(' ')
        param1 = int(param1)
        if param1 < len(friend_list["friends"]) and param1 >= 0 :
            print(f'{friend_list["friends"][param1]} changed his username to {param2}.')
            friend_list["friends"][param1] = param2
