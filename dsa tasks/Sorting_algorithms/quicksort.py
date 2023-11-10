def quicksort(nums,left,right):
    if left < right:
        parittionpos = partition(nums,left,right)
        print(nums,left,parittionpos-1)
        quicksort(nums,left,parittionpos-1)
        print(nums,parittionpos+1,right)
        quicksort(nums,parittionpos+1,right)
def partition(nums,left,right):
    i = left
    j = right - 1
    pivot=nums[right]

    while i < j:
        while i < right and nums[i] < pivot:
            i += 1
        while j > left and nums[j] >= pivot:
            j -=1

        if i<j:
            nums[i],nums[j]=nums[j],nums[i]

    if nums[i] > pivot:
        nums[i],nums[right]=nums[right],nums[i]

    return i


nums = [int(x) for x in input().split()]
quicksort(nums,0,len(nums)-1)
print(*nums,sep=' ')