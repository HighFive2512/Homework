gradeDict = {}
nrows = int(input())
for eachrow in range(nrows):
    input_name = input()
    input_grade = float(input())
    if input_name not in gradeDict:
        gradeDict[input_name] = [input_grade]
    else:
        gradeDict[input_name].append(input_grade)
gradeDict = {
    eachitem: (sum(eachgrade) / len(eachgrade))
    for eachitem, eachgrade in gradeDict.items()
}
[
    print(f'{stname} -> {"{:.2f}".format(avggrade)}')
    for stname, avggrade in gradeDict.items()
    if avggrade >= 4.50
]
