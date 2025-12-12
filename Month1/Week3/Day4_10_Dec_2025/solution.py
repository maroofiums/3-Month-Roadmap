def get_next_greater(nums):
    stack = []
    res = [-1]*len(nums)

    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            res[idx] = nums[i]
        stack.append(i)
    return res  

print(get_next_greater([1,3,4,2]))  
## output : [3,4,-1,-1]