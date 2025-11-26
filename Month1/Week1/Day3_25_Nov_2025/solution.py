def range_sum(arr, l, r):
    prefix = [0] * len(arr)
    prefix[0] = arr[0]

    for i in range(1, len(arr)):
        prefix[i] = prefix[i-1] + arr[i]

    if l == 0:
        return prefix[r]
    else:
        return prefix[r] - prefix[l-1]


arr = [2, 3, 4, 5, 6]
print(range_sum(arr, 1, 3))   
