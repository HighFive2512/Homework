userlist = input().split(", ")
for eachuser in userlist:
    if (
        3 <= len(eachuser) <= 16
        and all(
            eachletter.isalnum() or eachletter == "-" or eachletter == "_"
            for eachletter in eachuser
        )
        and not " " in eachuser
    ):
        print(eachuser)
