

## **Week 9 – Day 2 (19 Jan) → Pandas Basics (Deep + Practical)**

**Goal:**
Raw data ko clean, understand aur ML-ready banana.
Agar Pandas strong ho gaya → ML 70% easy ho jata hai.

---

## ⏱️ **Time Plan (2–3 hours)**

---

## **Hour 1: Pandas Fundamentals**

### 1️⃣ Import & Load Data

```python
import pandas as pd

df = pd.read_csv("titanic.csv")
```

### 2️⃣ First Look (VERY IMPORTANT)

```python
df.head()      # first 5 rows
df.tail()      # last 5 rows
df.info()      # data types + missing values
df.describe()  # statistics (mean, min, max)
```

🧠 **Why this matters?**
Interview + real ML mein **sab se pehla kaam** ye hota hai.

---

### 3️⃣ Columns & Rows Access

```python
df.columns
df["Age"]              # single column
df[["Age", "Fare"]]    # multiple columns
```

```python
df.iloc[0]     # first row (index-based)
df.loc[0]      # first row (label-based)
```

💡 **Best Practice:**

* `iloc` → index based
* `loc` → condition based (zyada use hota hai)

---

## **Hour 2: Data Cleaning (Real ML Skill)**

### 4️⃣ Missing Values Check

```python
df.isnull().sum()
```

### 5️⃣ Handle Missing Values

```python
# Fill Age with mean
df["Age"].fillna(df["Age"].mean(), inplace=True)

# Drop column (example)
df.drop(columns=["Cabin"], inplace=True)
```

🧠 **Advice:**

* Numerical → mean/median
* Categorical → mode
* Random fill ❌ (avoid)

---

### 6️⃣ Filtering Data

```python
# Passengers older than 30
df[df["Age"] > 30]

# Female passengers who survived
df[(df["Sex"] == "female") & (df["Survived"] == 1)]
```

💡 This logic will be **used in feature engineering** tomorrow.

---

## **Hour 3: Grouping & Basic Analysis**

### 7️⃣ GroupBy (VERY IMPORTANT)

```python
df.groupby("Sex")["Survived"].mean()
```

```python
df.groupby("Pclass")["Fare"].mean()
```

🧠 **Think like ML engineer:**
Is survival related to gender? class? fare?

---

### 8️⃣ Value Counts

```python
df["Sex"].value_counts()
df["Pclass"].value_counts()
```

Used for **class imbalance detection**.

---
