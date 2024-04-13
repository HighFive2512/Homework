def group_of_tens(tens):
    group, grouptwo = 0, 10
    while group < max(tens):
        tensnumbers = [nums for nums in tens if group < nums <= grouptwo]
        print(f"Group of {grouptwo}'s: {tensnumbers}")
        group += 10
        grouptwo += 10


numbers = [int(x) for x in input().split(", ")]
group_of_tens(numbers)
