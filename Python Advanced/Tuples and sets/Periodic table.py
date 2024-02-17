uinput = int(input())
unq_chems = set()
for each_input in range(uinput):
    chem_input = input().split(" ")
    for each_chem in chem_input:
        unq_chems.add(each_chem)

for every_unq_chem in unq_chems:
    print(every_unq_chem)