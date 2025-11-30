
# 📌 Day 7 — Arrays + Strings Combo (3 Medium Problems)

*Aaj hum 3 different patterns ko ek saath connect karenge — taake tumhari problem-solving “multi-weapon mode” mein aa jaye.*
Friendly mentor-style explanation neeche 👇

---

# 🔥 Problem 1: Two Sum (HashMap Trick)

### ⭐ Intuition (simple dosti style):

Bhai idea ye hai ke:

* Tum array traverse karo
* Har element ka “complement” check karo (`target - nums[i]`)
* Agar complement map me exist karta ho → answer mil gaya
* Warna current number ko map me store karlo

Yani ek dost list banayi hui hai, jisme tum puchhte ho:
**“Yaar, jiski mujhe zaroorat hai wo pehle se maujood hai?”**

---

### 🔹 Pseudocode:

```
map = empty hash
for i in 0..n:
    need = target - nums[i]
    if need in map:
        return [map[need], i]
    else:
        map[nums[i]] = i
```

### 💡 Honest Tip:

Brute-force avoid karo (O(n²)). Interviewers hashmap solution hi expect karte hain.

---

# 🔥 Problem 2: Maximum Subarray (Kadane’s Algorithm)

### ⭐ Intuition:

Bhai ye life-lesson type algorithm hai 😄
Idea:

* Agar tumhari current sum negative ho jaye → fresh start lo
* Nahi to usi ko grow karo
* Best sum track karte jao

Ye basically **“momentum maintain karo jab tak positive ho”** logic hai.

---

### 🔹 Pseudocode:

```
current = nums[0]
best = nums[0]

for i from 1 to n:
    current = max(nums[i], current + nums[i])
    best = max(best, current)

return best
```

### 💡 Honest Tip:

Kadane har array coder ka “default tool” hai — ise yaad rakhna hi rakhna.

---

# 🔥 Problem 3: Longest Substring Without Repeating Characters

(Ye tum Day 6 me seekh chuke ho — but ab arrays+strings combo day me integrate kar rahe)

### ⭐ Intuition:

* Set / map use karo
* Right pointer expand karta hai
* Duplicate mile → left clean karega
* Best window update karte jao

Sliding window ka “perfect warmup” problem.

---

### 🔹 Pseudocode:

```
window = empty set
left = 0
best = 0

for right in 0..len(s):
    while s[right] in window:
        remove s[left]
        left++

    add s[right]
    best = max(best, right - left + 1)

return best
```

---

# 🧠 Mini Notes To Add in GitHub

Tum apne repo me ye choti choti notes add kar sakte ho:

### ✔ Two Sum Note:

* HashMap = fastest lookup
* Single pass = best version

### ✔ Kadane Note:

* DP + greedy mixture
* Sirf “current best prefix” track karo

### ✔ Longest Substring:

* Classic variable window
* “Expand → fix → update” pattern

### ✔ Small Diagrams:

* Two Sum: arrows between indices
* Kadane: running sum graph
* Sliding Window: left/right pointer stretching diagram

---

# 📌 Summary (yaad rakho):

* HashMap problems = constant-time lookup ka magic
* Kadane = positive momentum, negative reset
* Sliding window = grow + shrink for validity
* Har pattern ko ek do baar likh kar dekh lena — muscle memory ban jayegi
