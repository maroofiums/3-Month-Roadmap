#  Problem 1: Two Sum --> Leetcode # 1

class Solution:
    def twoSum(self, nums, target):
        seen = {}  
        for i, num in enumerate(nums):
            need = target - num
            
            if need in seen:
                return [seen[need], i]

            seen[num] = i

#  Problem 2: Maximum Subarray --> Leetcode # 53

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = nums[0]

        for num in nums[1:]:
            curr_sum = max(num,curr_sum + num)
            max_sum = max(max_sum,curr_sum)

        return max_sum 

#  Problem 3: Longest Substring Without Repeating Characters --> Leetcode # 3

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        result = 0
        left = 0

        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            window.add(s[right])
            result = max(result,right-left+1)
        return result