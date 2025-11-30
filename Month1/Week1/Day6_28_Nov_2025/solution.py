# Problem1 --> Longest substring without repeating characters (Leetcode # 3)

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


