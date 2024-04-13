studentdict = {}
while True:
    uinput = input()
    if uinput.strip() == "end":
        for course_name, studentsnum in studentdict.items():
            print(f"{course_name}: {len(studentsnum)}")
            [print(f"-- {stname}") for stname in studentdict[course_name]]
        break
    else:
        uinput = uinput.strip().split(" : ")
        subject, studentname = uinput[0], uinput[1]
        if subject not in studentdict:
            studentdict[subject] = []
        studentdict[subject].append(studentname)
