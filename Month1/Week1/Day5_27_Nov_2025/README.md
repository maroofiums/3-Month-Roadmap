
# Month1 - Week1 - Day 5
**Date:** 27 Nov 2025

**Topic:** Strings Basics

**Focus:**  
- Reverse string manually & Python way  
- Palindrome check (single/multi-word)  
- Anagram check between two strings  
- String manipulation + comparison patterns  

---

## Problem / Exercise

### 1️⃣ Reverse String
Given: `"hello"`  
Output: `"olleh"`

**Ways:**  
1. Using slicing  
2. Using loop  

```python
# Slicing
s = "hello"
print(s[::-1])

# Loop
rev = ""
for ch in s:
    rev = ch + rev
print(rev)
````

---

### 2️⃣ Palindrome Check

Check if a string reads same backward and forward.

```python
s = "racecar"
print(s == s[::-1])  # True

# Optional: ignore spaces/case
s2 = "A man a plan a canal Panama".replace(" ", "").lower()
print(s2 == s2[::-1])
```

---

### 3️⃣ Anagram Check

Two strings have same letters (order doesn’t matter).

```python
from collections import Counter

s1 = "listen"
s2 = "silent"

print(Counter(s1) == Counter(s2))  # True
```

---

### Mini Experiment

1. Random string generator → check palindrome automatically
2. Count all anagrams of a word in a list of words
3. Test edge cases: empty string, single char, case differences

```python
import random, string

rand_str = ''.join(random.choices(string.ascii_lowercase, k=5))
print("Random string:", rand_str)
print("Is palindrome?", rand_str == rand_str[::-1])
```

---
