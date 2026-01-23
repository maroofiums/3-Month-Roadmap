## **Week 9 – Day 6 (23 Jan) → KNN (Deep + Practical)**

**Goal:**

* Distance-based classification samajhna
* Train & test KNN model
* Feature scaling ka importance practice karna

---

## ⏱️ **Time Plan (2–3 hours)**

---

### **Hour 1: Conceptual Understanding**

1️⃣ **KNN Kya Hai?**

* Predict **class of a point** based on **closest neighbors**
* “Nearby passengers ka survival kaisa tha?” → Decide new passenger survival
* Non-parametric model → no explicit training, **just store training data**

2️⃣ **Hyperparameters**

* `n_neighbors` → kitne neighbors check karein
* `weights` → uniform or distance
* **Distance metric:** Euclidean (default)

💡 **Tip:** Scaling **must** hai kyunki distance sensitive hai

---

### **Hour 2: Train KNN Model**

Assume **Day 3 features ready** (`X_train, X_test, y_train, y_test`)

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

knn = KNeighborsClassifier(n_neighbors=3)  # 3 nearest neighbors
knn.fit(X_train, y_train)

y_pred_knn = knn.predict(X_test)
```

---

### **Hour 3: Evaluate + Experiment**

1️⃣ **Accuracy + Confusion Matrix**

```python
print("Accuracy:", accuracy_score(y_test, y_pred_knn))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_knn))
```

2️⃣ **Experiment with neighbors**

```python
for k in [1,3,5,7]:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    print(f"K={k}, Accuracy={accuracy_score(y_test,y_pred)}")
```

3️⃣ **Optional: Weighted KNN**

```python
knn = KNeighborsClassifier(n_neighbors=5, weights='distance')
knn.fit(X_train, y_train)
print("Weighted KNN Accuracy:", accuracy_score(y_test, knn.predict(X_test)))
```

---

### **Mini Practice (Must Do)**

* Try changing `n_neighbors` → observe accuracy
* Remove scaling → observe big drop in accuracy
* Predict **single passenger** survival

```python
sample = X_test[0].reshape(1,-1)
print(knn.predict(sample))
```

---

### ❌ **Common Mistakes**

* Skip scaling → distance wrong ❌
* Too large/small `k` → under/overfitting ❌
* Use categorical features without encoding ❌

---

### ✅ **Day 6 Takeaways**

1. KNN = distance-based, simple, intuitive
2. Feature scaling **must** for distance models
3. n_neighbors tuning → model performance
4. Weighted KNN → better predictions in imbalanced data

---