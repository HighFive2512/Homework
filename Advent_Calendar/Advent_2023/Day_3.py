import sys
import re

nums = 0
pattern = r'\d+'
symbol_pattern = r'[\!\"\#\$\%\&\'\(\)\*\+\,\-\/\:\;\<\=\>\?\@\]\[\^\_\`\{\|\}\~\\]'
gear_pattern = r'(\d+\*\d+)'
gear_nums = 0
with open('D:\GIT_stuff\Homework\Homework\Advent_Calendar\Advent_2023\day_3_input.txt', 'r',encoding='utf-16') as file:
    advent_task_content = file.read().strip()
    i = 0
    while True:
        line = advent_task_content.split('\n')
        if i == int(len(line)):
            break
        current_line = line[i]
        prev_line = line[i - 1] if i > 0 else None
        next_line = line[i + 1] if i < (len(line) - 1) else None
        next_next_line = line[i + 2] if i < (len(line) - 1) else None

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
            digit = int(current_line[each_digit_set.start():each_digit_set.end()])
            if re.search(symbol_pattern, current_line[current_start_idx:current_end_idx]):
                nums += digit
                continue
            # check for previous line

            if prev_line != None :
                prev_line_match = prev_line[current_start_idx:current_end_idx]
                if re.search(symbol_pattern,prev_line_match):
                    nums += digit
                    continue
            #check for next line
            if next_line != None:
                next_line_match = next_line[current_start_idx:current_end_idx]
                if re.search(symbol_pattern,next_line_match):
                    if re.search(r'\*',next_line_match) and next_next_line != None:

                    nums += digit
                    continue

        i += 1
print(nums)