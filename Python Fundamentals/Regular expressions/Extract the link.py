import re

while True:

    userinput = input()
    if userinput != "":
        userinput = userinput.split(" ")
        for eachwrd in userinput:
            check_if_is_link = re.match(
                r"^w{3}\.([A-Za-z0-9\-]+)(\.[A-Za-z]+)", eachwrd
            )
            if check_if_is_link:
                print(eachwrd)
    else:
        break
