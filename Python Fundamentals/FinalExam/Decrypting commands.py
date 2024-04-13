basic_str = input()
while True:
    decrypting_command = input().strip()
    if decrypting_command == "Finish":
        break
    decrypting_command = decrypting_command.split(" ")
    command = decrypting_command[0]

    if command == "Replace":
        argument1, argument2 = decrypting_command[1], decrypting_command[2]
        basic_str = "".join(argument2 if x == argument1 else x for x in basic_str)
        print(basic_str)
    if command == "Cut":
        argument1, argument2 = (
            int(decrypting_command[1]),
            int(decrypting_command[2]) + 1,
        )
        if len(basic_str) >= argument2:
            basic_str = basic_str[:argument1] + basic_str[argument2:]
            print(basic_str)
        else:
            print("Invalid indices!")
    if command == "Make":
        argument1 = decrypting_command[1]
        if argument1 == "Upper":
            basic_str = basic_str.upper()
        elif argument1 == "Lower":
            basic_str = basic_str.lower()
        print(basic_str)
    if command == "Check":
        argument1 = decrypting_command[1]
        if argument1 in basic_str:
            print(f"Message contains {argument1}")
        else:
            print(f"Message doesn't contain {argument1}")
    if command == "Sum":
        argument1, argument2 = (
            int(decrypting_command[1]),
            int(decrypting_command[2]) + 1,
        )
        if argument1 > 0 and argument2 > 0 and len(basic_str) >= argument2:
            print(sum(ord(s) for s in basic_str[argument1:argument2]))
        else:
            print("Invalid indices!")
