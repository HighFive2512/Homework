import sys
import re

nums = 0
pattern = r'\d+'
symbol_pattern = r'[!"#$%&\'()*+,\-/:;<=>?@[\\]^_`{|}~]'

with open(sys.argv[1], 'r',encoding='utf-16') as file:
    advent_task_content = file.read().strip()
    i = 0
    while True:
        line = advent_task_content.split('\n')
        if i == int(len(line)):
            break
        current_line = line[i]
        prev_line = line[i - 1] if i > 0 else None
        next_line = line[i + 1] if i < len(line) - 1 else None
        check_for_digits = re.finditer(pattern, current_line)
        for each_digit_set in check_for_digits:

            # check for current line
            if each_digit_set.start() == 0:
                current_start_idx = 0
            else:
                current_start_idx = each_digit_set.start() - 1

            if each_digit_set.end() == len(current_line):
                current_end_idx = each_digit_set.end()
            else:
                current_end_idx = each_digit_set.end() + 1

            if re.match(symbol_pattern, current_line[current_end_idx:current_end_idx]):
                print(current_line[each_digit_set.start():each_digit_set.end()])
                nums += int(current_line[each_digit_set.start():each_digit_set.end()])
                break

            # check for previous line
            if prev_line != None:
                if re.match(symbol_pattern,prev_line[current_start_idx:current_end_idx]):
                    print(current_line[each_digit_set.start():each_digit_set.end()])
                    nums += int(current_line[each_digit_set.start():each_digit_set.end()])
                    break
            #check for next line
            if next_line != None:
                if re.match(symbol_pattern, next_line[current_start_idx:current_end_idx]):
                    print('nextlineree')
                    nums += int(current_line[each_digit_set.start():each_digit_set.end()])
                    break

        i += 1
print(nums)