### Brute Force
## O(n^2)
def twosumslow(nums:list,target:int) -> int:
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    
    return -1

### Hashmap
## O(1)
def twosumfast(nums:list,target:int) -> int:
    hashmap = {}

    for i,num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement],i]
        hashmap[num] = i 


import random, time
nums = random.sample(range(1000000), 10000)
target = nums[123] + nums[456]

start = time.time()
twosumslow(nums,target)
end = time.time()
print("Brute-Force taken:", end-start)

start = time.time()
twosumfast(nums,target)
end = time.time()
print("Hashmap taken:", end-start)
