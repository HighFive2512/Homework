def insertionalgo(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1


arr = [int(x) for x in input().split()]
resalt = insertionalgo(arr)
print(*arr, sep=" ")
