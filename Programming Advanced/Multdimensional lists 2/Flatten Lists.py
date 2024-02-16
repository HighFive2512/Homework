l1 = input().split("|")

sub_l = []

for sub_str in l1[::-1]:
    sub_l.extend(sub_str.split())


print(*sub_l)
