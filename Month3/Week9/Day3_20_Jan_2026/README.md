

## **Week 9 – Day 3 (20 Jan) → Feature Engineering (Deep + Practical)**

**Goal:**
Raw data ➜ clean ➜ numerical ➜ scaled ➜ ML-ready

> Model se pehle **features powerful honi chahiye**.

---

## ⏱️ **Time Plan (2–3 hours)**

---

## **Hour 1: Categorical → Numerical (Encoding)**

ML models **strings nahi samajhte**, sirf numbers.

### 1️⃣ Identify categorical columns

```python
df.select_dtypes(include="object").columns
```

Titanic mein usually:

* Sex
* Embarked

---

### 2️⃣ Label Encoding (Binary case)

```python
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df["Sex"] = le.fit_transform(df["Sex"])
```

🧠 Result:

* male → 1
* female → 0

**Use when:** sirf 2 categories ho.

---

### 3️⃣ One-Hot Encoding (Best Practice)

```python
df = pd.get_dummies(df, columns=["Embarked"], drop_first=True)
```

🧠 **Why drop_first?**
Multicollinearity avoid hoti hai.

✅ **Best Practice:**

* Binary → LabelEncoder
* Multiple categories → One-Hot Encoding

---

## **Hour 2: Feature Selection + Scaling**

### 4️⃣ Select Features & Target

```python
X = df[["Age", "Fare", "Sex", "Pclass"]]
y = df["Survived"]
```

❌ **Avoid:**

* PassengerId
* Name
* Ticket

(Ye ML ko confuse karte hain)

---

### 5️⃣ Feature Scaling (VERY IMPORTANT)

Especially for **Logistic Regression & KNN**

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

🧠 **What scaling does?**

* Mean = 0
* Std = 1
* Large values dominance khatam

---

### 6️⃣ Train-Test Split

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)
```

🧠 **Rule:**
Never train & test on same data ❌

---

## **Hour 3: Feature Insight + Practice**

### 7️⃣ Feature Importance (Manual Thinking)

Ask yourself:

* Age survival ko affect karta?
* Fare rich vs poor?
* Gender impact?

ML engineer **logic bhi lagata hai**, sirf code nahi.

---

### 🧪 **Mini Practice (Must Do)**

```python
print("Train shape:", X_train.shape)
print("Test shape:", X_test.shape)
print("Target distribution:\n", y.value_counts(normalize=True))
```

---

## ❌ **Common Mistakes**

* Scaling ke baad `y` ko scale karna ❌
* Train-test split se pehle scaling ❌
* Random columns add kar dena ❌

---

## ✅ **Day 3 Takeaways**

* Feature engineering > model choice
* Encoding converts language → numbers
* Scaling is compulsory for distance-based models
* Clean features = stable ML pipeline

---
