examRes = {}
bannedlist = []
submissionlist = {}
while True:
    uinput = input()
    if uinput.strip() == "exam finished":
        break
    uinput = uinput.split("-")
    if uinput[1] == "banned":
        bannedlist.append(uinput[0])
    else:
        username, language, points = uinput[0], uinput[1], uinput[2]
        if uinput[1] not in submissionlist.keys():
            submissionlist[uinput[1]] = 1
        else:
            submissionlist[uinput[1]] = submissionlist[uinput[1]] + 1
        if language not in examRes:
            examRes[language] = [f"{username} : {points}"]
        else:
            idx = [ind for ind, x in enumerate(examRes[language]) if username in x]
            if idx:
                idx = int(idx[0])
                splitput = examRes[language][idx].split(" : ")
                if int(splitput[1]) < int(points):
                    examRes[language][idx] = f"{username} : {points}"
            else:
                examRes[language] += [f"{username} : {points}"]

print("Results:")
[
    print(f"{usrname} | {pts} ")
    for content_list in examRes.values()
    for content in content_list
    for usrname, pts in [content.split(" : ")]
    if usrname not in bannedlist
]
print("Submissions:")
[print(f"{lang} - {submissionlist[lang]}") for lang in examRes]
