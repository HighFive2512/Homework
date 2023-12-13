import re

symbol_pattern = r'[?(*)?]'


string = '..*..'

# check_for_digits = re.finditer(r'\d+', string)
# for eachdigit in check_for_digits:
#     start = eachdigit.start() -1
#     end = eachdigit.end() +1
#     check = re.match(symbol_pattern,string[start:end])
#     print(check)

checkforsym = re.search(symbol_pattern,string)
print(checkforsym)