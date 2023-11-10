def mergesort(nums):
    if len(nums) > 1:
        firsthalf = nums[:len(nums)//2]
        secondhalf = nums[len(nums)//2:]

        mergesort(firsthalf)
        mergesort(secondhalf)

        ind1 = 0
        ind2 = 0
        mergind = 0
        while ind1 < len(firsthalf) and ind2 < len(secondhalf):
            if firsthalf[ind1] < secondhalf[ind2]:
                nums[mergind] = firsthalf[ind1]
                ind1 +=1
            else:
                nums[mergind] = secondhalf[ind2]
                ind2 +=1
            mergind +=1

        while ind1 < len(firsthalf):
            nums[mergind] = firsthalf[ind1]
            ind1 += 1
            mergind +=1

        while ind2 < len(secondhalf):
            nums[mergind] = secondhalf[ind2]
            ind2 +=1
            mergind +=1

nums = [int(x) for x in input().split()]
mergesort(nums)
print(*nums,sep=' ')