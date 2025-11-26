
# Month1 - Week1 - Day 3
**Date:** 25 Nov 2025

**Topic:** Prefix Sum (Arrays)

**Focus:**  
- Prefix sum kya hota hai aur kyun use hota hai  
- O(n²) → O(n) optimization feel karna  
- Range sum fast calculate karna  
- Subarray problems ki foundation banana  

---

## Problem / Exercise:

### 1️⃣ Basic Prefix Sum Build
Given:
```python
arr = [1, 2, 3, 4]
````

Build prefix array:

```python
# Output: [1, 3, 6, 10]
```

---

### 2️⃣ Range Sum Query (Fast)

Find sum from index **l to r**:

Example:

```
arr = [1,2,3,4,5]
l = 1
r = 3
Sum = 2+3+4 = 9
```

Prefix trick:

```
prefix[r] - prefix[l-1]
```

---

### 3️⃣ Subarray Sum Check

Check if any subarray has sum = target:

Example:

```
arr = [3, 4, -7, 1, 3, 3, 1, -4]
target = 7
```

---

### 4️⃣ Mini Problems to Solve

1. Build prefix sum array
2. Given array + queries, find multiple range sums fast
3. Given array, check if **any subarray = target sum**
4. Bonus: Count subarrays with sum = target (Prefix + Hashmap)

---

## Notes / Mini Experiment

### 🔹 Build Prefix Sum (Step-by-step)

```python
arr = [1, 2, 3, 4]
prefix = [0] * len(arr)

prefix[0] = arr[0]
for i in range(1, len(arr)):
    prefix[i] = prefix[i-1] + arr[i]

print(prefix)  # [1, 3, 6, 10]
```

---

### 🔹 Fast Range Sum

```python
l = 1
r = 3
range_sum = prefix[r] - prefix[l-1]
print(range_sum)
```

---

### 🔹 Subarray Sum = Target (Best Prefix + Hashmap Trick)

```python
arr = [3, 4, -7, 1, 3, 3, 1, -4]
target = 7

prefix = 0
seen = {0: 1}

for num in arr:
    prefix += num
    if prefix - target in seen:
        print("Found subarray with target sum")
        break
    seen[prefix] = 1
```

---

