def available_chairs(chairs, visitors, rnum):
    global chairsleft, flag
    visitors = int(visitors)
    if len(chairs) < visitors:
        print(f"{visitors-len(chairs)} more chairs needed in room {rnum}")
        flag = "y"
    elif len(chairs) > visitors:
        chairsleft += len(chairs) - visitors


flag = "n"
uinput = int(input())
chairsleft = 0
for i in range(1, uinput + 1):
    chairs_visitors = input()
    c, v = chairs_visitors.split(" ")
    available_chairs(c, v, i)

if chairsleft >= 0 and flag == "n":
    print(f"Game On, {chairsleft} free chairs left")
