from collections import deque
def sliding_window_max(nums, k):
    dq = deque()
    res = []

    for i in range(len(nums)):
        if dq and dq[0] == i - k:
            dq.popleft()
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res

print(sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3))

