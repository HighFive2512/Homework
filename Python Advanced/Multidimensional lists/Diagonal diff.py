nums = int(input())

first_Res, second_Res = 0, 0

for i in range(nums):
    line = [int(x) for x in input().split()]
    first_Res += line[i]
    second_Res += line[nums - i - 1]

print(abs(first_Res - second_Res))