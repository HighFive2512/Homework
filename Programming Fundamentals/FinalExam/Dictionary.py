import re

dict_string = input()
keywords_check = input()
teacher_input = input().strip()

keywords = re.findall(r'\|?([\w+]+)\s?:\s?([\w+\s\,]+)', dict_string)
lib_dict = {}
order_of_appearance = []
for word, definition in keywords:
    if word not in lib_dict:
        lib_dict[word] = []
        order_of_appearance.append(word)
    lib_dict[word].append(definition.strip())

if teacher_input == "Test":
    for word_to_test in keywords_check.split(' | '):
        if word_to_test in lib_dict:
            print(f'{word_to_test}:')
            for definition in lib_dict[word_to_test]:
                print(f' -{definition}')

if teacher_input == "Hand Over":
    words_to_print = [word for word in order_of_appearance if word in lib_dict]
    if words_to_print:
        print(' '.join(words_to_print))
