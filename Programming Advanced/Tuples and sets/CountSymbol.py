chars_amount = {}

for each_char in input():
    if each_char not in chars_amount:
        chars_amount[each_char] = 1
    else:
        chars_amount[each_char] += 1

#chars_amount = dict(sorted(chars_amount.items()))

for each_key,each_val in sorted(chars_amount.items()):
    print(f'{each_key}: {each_val} time/s')