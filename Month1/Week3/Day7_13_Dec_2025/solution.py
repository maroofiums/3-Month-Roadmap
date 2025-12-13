
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap,num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return min_heap[0]

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        result = [0] * len(temperatures)


        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                result[idx] = i-idx
            stack.append(i)

        return result

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        for char in s:
            if char in mapping.values():
                stack.append(char)
            else:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
        
        return len(stack) == 0
