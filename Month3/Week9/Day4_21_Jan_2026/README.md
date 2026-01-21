

## **Week 9 – Day 4 (21 Jan) → Logistic Regression (Deep + Practical)**

**Goal:**
Feature-engineered data par **Logistic Regression train**, test aur evaluate karna — *proper ML workflow ke sath*.

---

## ⏱️ **Time Plan (2–3 hours)**

---

## **Hour 1: Logistic Regression Concept (Simple Language)**

### 🧠 Logistic Regression kya hai?

* Binary classification ke liye use hota hai
* Output: **0 or 1** (Yes/No, Survived/Not Survived)
* Inside: **Sigmoid function** (0–1 probability)

Think like this 👇

> “Passenger survive karega ya nahi?”

---

### 📐 Mathematical intuition (light)

* Linear combination: `z = wX + b`
* Sigmoid: `1 / (1 + e^-z)`
* Probability > 0.5 → class 1

❌ Maths mein mat phanso
✅ Concept clear rakho

---

## **Hour 2: Train Logistic Regression Model**

Assuming **Day 3 ka data ready hai**
(`X_train, X_test, y_train, y_test`)

### 1️⃣ Import & Train Model

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)
```

🧠 Internally:

* Weights learn ho rahe hain
* Best decision boundary find ho rahi hai

---

### 2️⃣ Predictions

```python
y_pred = model.predict(X_test)
```

---

## **Hour 3: Model Evaluation (MOST IMPORTANT)**

### 3️⃣ Accuracy

```python
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
```

❗ **Warning:**
High accuracy ≠ good model (class imbalance ka issue)

---

### 4️⃣ Confusion Matrix

```python
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)
print(cm)
```

Matrix samjho 👇

```
[[TN FP]
 [FN TP]]
```

* TP → Correct survival
* FP → Galat survival
* FN → Missed survival

🧠 ML engineer **errors samajhta hai**, sirf accuracy nahi dekhta.

---

### 5️⃣ Classification Report

```python
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))
```

Ismein milega:

* Precision
* Recall
* F1-score

📌 **Interview favorite output**

---

## 🧪 **Mini Practice (Must Do)**

```python
# Try changing C value
model2 = LogisticRegression(C=0.5)
model2.fit(X_train, y_train)
print("New Accuracy:", accuracy_score(y_test, model2.predict(X_test)))
```

🧠 `C` = regularization strength

* Small C → simple model
* Large C → complex model

---

## ❌ **Common Mistakes**

* Feature scaling skip karna ❌
* Sirf accuracy dekhna ❌
* Train data pe hi test karna ❌

---

## ✅ **Day 4 Takeaways**

* Logistic Regression = ML ka base model
* Binary classification ke liye best
* Confusion matrix > accuracy
* Proper evaluation = professional ML

