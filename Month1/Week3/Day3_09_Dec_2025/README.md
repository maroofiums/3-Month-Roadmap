
# **📘 Day 3 – Valid Parentheses**

**Date:** 9 Dec 2025
**Topic:** Valid Parentheses
**Focus:** Stack usage
**Problem:** LeetCode – Valid Parentheses

---

## **🔥 Concept – Is problem ka real meaning (friendly explanation)**

Socho tum code likh rahe ho, aur braces `{}`, brackets `[]`, parentheses `()` properly close nahi hain.
Compiler confuse ho jata hai.

Ye problem exactly wohi check karti hai:

👉 Brackets **correctly open hon**
👉 Aur **correct order me close hon**

Examples:

```
"()"      → valid  
"()[]{}"  → valid  
"(]"      → ❌ invalid  
"([)]"    → ❌ invalid  
"{[]}"    → valid  
```

---

## **💡 Logic (Urdu + English mix, super clear)**

Jab bhi koi opening bracket mile → stack me push.
Jab closing bracket mile → stack ka last opening bracket uska matching pair hona chahiye.

Agar mismatched? → invalid
Agar end me stack empty nahi? → invalid
Agar sab perfect? → valid ✔️

---

## **🧠 Pseudocode (simple + neat)**

```
make an empty stack

for each char in string:
    if char is opening bracket:
        push to stack
    
    else if char is closing:
        if stack empty:
            return false
        
        pop from stack and check:
            closing must match with popped opening
        if not matched:
            return false

after loop:
    if stack empty:
        return true
    else:
        return false
```

---

## **💻 Python Code (clean + interview-friendly)**

```python
def isValid(s):
    stack = []
    match = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack:
                return False
            
            if stack.pop() != match[ch]:
                return False

    return len(stack) == 0
```

---

## **🧪 Mini Experiment**

Try these inputs manually:

### Test 1:

```
Input: "()"
Stack flow:
push '('
closing ')' → match '(' ✔️
Final stack empty → valid
```

### Test 2:

```
Input: "(]"
Flow:
push '('
closing ']' → top is '(' → mismatch ❌
```

### Test 3:

```
Input: "([{}])"
Flow:
push '('
push '['
push '{'
closing '}' → matches '{'
closing ']' → matches '['
closing ')' → matches '('
Stack empty → valid ✔️
```

---

