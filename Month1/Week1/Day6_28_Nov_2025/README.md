

# 📌Day 6 **28 Nov – Sliding Window (Concept + Intuition + Pseudocode Only)**

Friendly mentor-style explanation (Urdu + English mix) 👇

---

## ⭐ Sliding Window — Why it Exists?

Bhai, idea simple hai:

**Tum string/array ko ek “chalti hui khidki” se dekhte ho.**
Right pointer window ko **expand** karta hai.
Left pointer window ko **shrink** karta hai.

Jab tak window valid hai → expand
Jab window invalid ho jaye → shrink

Bas ye hi sliding window ka pura game.

---

# 🔥 Problem 1: Longest Substring Without Repeating Characters

(LeetCode #3 – Best intro sliding window)

### **Intuition (dosti style):**

* Tum ek set rakhte ho jisme current window ke characters store hote hain
* Right pointer new char add karta hai
* Agar repeat mil jaye → left pointer hata-hata ke duplicate remove karta hai
* “Best length” update karte jao

Itna hi hai.

---

## **Pseudocode (Simple Urdu-English mix):**

```
window = empty set
left = 0
best = 0

for right in range(0, len(s)):
    while s[right] already in window:
        remove s[left] from window
        left++

    add s[right] in window
    best = max(best, right - left + 1)

return best
```

Isme koi rocket science nahi — repeat milne par window ko compress karna hota hai.

---

# 🔥 Problem 2: Max in Sliding Window (Fixed window)

Window size fixed hoti hai, e.g., k = 3

### **Intuition:**

* Fixed window me left pointer automatic hota hai → `i - k + 1`
* Tumko har window ka max chahiye
* Naive approach: har window ka max nikalna (O(n*k))
* Optimal: **deque** use karo → decreasing order me store karo
* Window se bahar hone wale indexes ko pop karo

### **Pseudocode:**

```
deque = empty

for i in each index:
    # Remove from back while nums[i] is larger
    while deque not empty AND nums[i] > nums[deque.last]:
        deque.pop()

    deque.push(i)

    # Remove front if it goes out of window
    if deque.first == i - k:
        deque.pop_front()

    # If window size >= k, record max (deque.first)
```

---

# 🔥 Bonus: Variable Window Pattern

Smallest substring containing all chars (classic pattern)

### **Pseudocode:**

```
need = count of target chars
window_count = {}
left = 0

for right in range(n):
    include s[right] in window_count

    while window valid:
        update result
        remove s[left]
        left++
```

---

# 📌 **Quick Summary (yaad rakho):**

* Right pointer = window ko aage badhata
* Left pointer = window ko clean/valid banata
* Fixed window = size constant
* Variable window = condition-based
* Longest substring w/o repeat = sliding window ka father pattern

---
