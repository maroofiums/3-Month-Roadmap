
# Month1 - Week1 - Day 4
**Date:** 26 Nov 2025

**Topic:** Max Subarray (Kadane’s Algorithm)

**Focus:**  
- Max subarray sum ki intuition samajhna  
- Kadane vs brute-force difference  
- Negative arrays me behavior  
- Running sum vs global max concept  

---

## Problem / Exercise

### 1️⃣ Classic Max Subarray Problem
Given:
```

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

```
Output:
```

6

# because subarray [4, -1, 2, 1]

```

---

### 2️⃣ Edge Case  
Pure negative array:
```

arr = [-5, -2, -8, -3]

```
Output:
```

-2

# (largest negative number)

````

---

### 3️⃣ Write Both Solutions  
1. Brute-force (O(n²)) → to understand  
2. Kadane optimized (O(n)) → real solution

---

## Notes / Mini Experiment

### 🔹 Brute Force (Understanding)
```python
arr = [-2,1,-3,4,-1,2,1,-5,4]
max_sum = float('-inf')

for i in range(len(arr)):
    curr = 0
    for j in range(i, len(arr)):
        curr += arr[j]
        max_sum = max(max_sum, curr)

print("Brute Force:", max_sum)
````

---

### 🔹 Kadane’s Algorithm (O(n))

```python
arr = [-2,1,-3,4,-1,2,1,-5,4]

current = arr[0]
best = arr[0]

for x in arr[1:]:
    current = max(x, current + x)
    best = max(best, current)

print("Kadane:", best)
```

---

### 🔹 Visual Intuition

* `current` = aaj ka best subarray jo abhi tak chal raha
* `best` = overall best jo kabhi mila
* Jab current negative ho jaye → restart from next element

---

## Mini Challenges

1. Kadane using `for` loop (without slicing)
2. Print the actual subarray (store start/end index)
3. Try random arrays of size 10k and see O(n) speed
4. What if we want **min subarray sum**? (reverse Kadane)

---

