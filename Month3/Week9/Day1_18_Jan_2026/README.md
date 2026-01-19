
## **Week 9 – Day 1 (18 Jan) → Numpy Basics**

**Goal:** Learn arrays, vectorized operations, indexing, and reshaping. Numpy is the **foundation for all ML computations**, so understand it deeply.

### **Time-Sliced Plan (2–3 hours)**

---

### **Hour 1: Numpy Basics**

1. **Import Numpy**

```python
import numpy as np
```

2. **Create arrays**

```python
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([[1,2,3],[4,5,6]])
print("1D array:", arr1)
print("2D array:\n", arr2)
```

3. **Check shape & dimensions**

```python
print("Shape of arr2:", arr2.shape)
print("Number of dimensions:", arr2.ndim)
```

4. **Array attributes**

```python
print("Datatype:", arr2.dtype)
print("Size:", arr2.size)
```

**Tip:** Think of **shape & ndim** as “size & structure” of your dataset for ML.

---

### **Hour 2: Indexing, Slicing, Reshaping**

1. **Indexing & Slicing**

```python
print("First element:", arr1[0])
print("Slice:", arr1[1:3])
print("2D indexing:", arr2[1,2])  # row 1, col 2
```

2. **Negative indexing**

```python
print("Last element:", arr1[-1])
```

3. **Reshaping arrays**

```python
arr3 = np.arange(1, 13)  # 1 to 12
arr3_reshaped = arr3.reshape(3,4)
print("Reshaped array:\n", arr3_reshaped)
```

4. **Flattening**

```python
print("Flattened:", arr3_reshaped.ravel())
```

**Tip:** Reshaping is essential for feeding data into ML models. Models expect consistent shapes.

---

### **Hour 3: Vectorized Operations & Random Numbers**

1. **Vectorized operations**

```python
a = np.array([1,2,3])
b = np.array([4,5,6])
print("Addition:", a+b)
print("Multiplication:", a*b)
print("Square:", a**2)
```

2. **Universal functions**

```python
print("Square root:", np.sqrt(a))
print("Exponential:", np.exp(a))
print("Mean:", np.mean(a))
```

3. **Random arrays**

```python
rand_arr = np.random.rand(3,3)  # 3x3 random numbers [0,1)
print(rand_arr)

rand_ints = np.random.randint(1,10,size=(2,4))  # integers 1-9
print(rand_ints)
```

**Mini Exercise (practice)**

```python
# Create array 1-10, reshape to 2x5, multiply by 2, print sum of columns
arr = np.arange(1,11).reshape(2,5)
arr = arr*2
print("Sum of columns:", arr.sum(axis=0))
```

---

### **Optional Challenge (Extra Learning)**

* Try `np.linspace(0,1,5)` → create 5 numbers evenly spaced between 0 and 1
* Use `np.eye(3)` → create identity matrix 3x3
* Understand broadcasting:

```python
a = np.array([[1,2,3],[4,5,6]])
b = np.array([1,2,3])
print("Broadcasted addition:\n", a+b)
```

**Tip:** Numpy is all about **doing operations without loops**. This is the main skill ML depends on for speed.

---
