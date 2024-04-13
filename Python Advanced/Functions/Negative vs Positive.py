from typing import List


def print_numbers(nums: List[int]) -> None:
    positive = sum(num for num in nums if num > 0)
    negative = sum(num for num in nums if num < 0)

    print(negative)
    print(positive)

    if positive > abs(negative):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


nums = [int(x) for x in input().split()]
print_numbers(nums)
