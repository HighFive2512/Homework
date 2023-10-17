uinput = input()

positive = [int(x) for x in uinput.split(", ") if int(x) >= 0 ]
negative = [int(x) for x in uinput.split(", ") if int(x) < 0 ]
even = [int(x) for x in uinput.split(", ") if int(x) % 2 == 0 ]
odd =[int(x) for x in uinput.split(", ") if int(x) % 2 == 1 ]

print(f'Positive: {", ".join(map(str, positive))}')
print(f'Negative: {", ".join(map(str, negative))}')
print(f'Even: {", ".join(map(str, even))}')
print(f'Odd: {", ".join(map(str, odd))}')