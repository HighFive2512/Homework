companyDict = {}
while True:
    comp_names = input()
    if comp_names.strip().lower() == 'end':
        break
    comp_names = comp_names.split(' -> ')
    emp_ids = comp_names[1]
    comp_names = comp_names[0]
    if comp_names not in companyDict or emp_ids not in companyDict[comp_names]:
        if comp_names not in companyDict:
            companyDict[comp_names] = [emp_ids]
        else:
            companyDict[comp_names].append(emp_ids)
for comps, idlist in companyDict.items():
    print(comps)
    [print('\n'.join([f'-- {ids}' for ids in idlist]))]