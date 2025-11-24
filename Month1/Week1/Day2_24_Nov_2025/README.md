# Month1 - Week1 - Day 2
**Date:** 24 Nov 2025

**Topic:** Two Sum (Arrays / Hashmap)

**Focus:**  
- Understand Two Sum problem step-by-step  
- Brute-force vs optimized (hashmap) approach  
- Python dict use karke O(n) solution feel karna  

**Problem / Exercise:**  
1. Brute-force approach: check all pairs in array  
2. Optimized approach: use dict/hashmap to store previous numbers  
3. Example:  
```python
nums = [2, 7, 11, 15]
target = 9
# Output: [0, 1]
````

4. Optional: try large random arrays to see performance difference

**Notes / Mini Experiment:**

* Mini Experiment: measure time for brute-force vs hashmap using large arrays

```python
import random, time
nums = random.sample(range(1000000), 10000)
target = nums[123] + nums[456]

start = time.time()
# Brute-force (optional small size only)
end = time.time()
print("Time taken:", end-start)
```

**Summary / Tip:**

* Two Sum = classic DSA pattern; many future problems me use hota hai
* Brute-force se shuru karo → optimized dict se finish
* Always visualize intermediate steps for better understanding

