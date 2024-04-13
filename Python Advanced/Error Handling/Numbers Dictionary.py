num_dict = {}

l = input()

while l != "Search":
    number_as_string = l

    try:
        num = int(input())
        num_dict[number_as_string] = num
    except ValueError:
        print("The variable number must be an integer")

    l = input()
l = input()

while l != "Remove":
    searched = l

    try:
        print(num_dict[searched])
    except KeyError:
        print("Number does not exist in dictionary")

    l = input()
l = input()

while l != "End":
    searched = l
    try:
        del num_dict[searched]
    except KeyError:
        print("Number does not exist in dictionary")

    l = input()
print(num_dict)
