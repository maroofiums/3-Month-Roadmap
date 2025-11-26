def kadane(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        print(f"{current_sum} -> current_sum")
        max_sum = max(max_sum, current_sum)
        print(f"{max_sum} -> max_sum")

    return max_sum

arr = [-2,1,-3,4,-1,2,1,-5,4]
print(kadane(arr))
