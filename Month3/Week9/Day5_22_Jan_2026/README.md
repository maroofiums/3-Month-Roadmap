

## **Week 9 – Day 5 (22 Jan) → Decision Tree (Deep + Practical)**

**Goal:**
Decision Tree train karna, visualize karna aur interpret karna. ML ke **feature importance concepts** bhi samajhna.

---

## ⏱️ **Time Plan (2–3 hours)**

---

### **Hour 1: Conceptual Understanding**

1️⃣ **Decision Tree Kya Hai?**

* Tree structure: **nodes, branches, leaves**
* Nodes → feature splits
* Leaves → prediction
* Works for **classification & regression**

2️⃣ **Split Decision:**

* Use **Gini Impurity** or **Entropy**
* Decide best feature to split data

> Think: “Passenger ka survival gender, age, class ke basis pe kaise decide hota?”

---

### **Hour 2: Train Decision Tree**

Assume **Day 3 ka features ready hai**
(`X_train, X_test, y_train, y_test`)

```python
from sklearn.tree import DecisionTreeClassifier

tree_model = DecisionTreeClassifier(max_depth=3, random_state=42)
tree_model.fit(X_train, y_train)
```

* `max_depth=3` → prevent overfitting
* `random_state=42` → reproducibility

---

### **Hour 3: Predictions + Evaluation + Visualization**

#### 1️⃣ Predict

```python
y_pred_tree = tree_model.predict(X_test)
```

#### 2️⃣ Evaluate

```python
from sklearn.metrics import accuracy_score, confusion_matrix

print("Accuracy:", accuracy_score(y_test, y_pred_tree))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_tree))
```

#### 3️⃣ Visualize Tree

```python
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))
plot_tree(
    tree_model,
    feature_names=['Age','Fare','Sex','Pclass'],
    class_names=['Not Survived','Survived'],
    filled=True
)
plt.show()
```

✅ **Tip:**
Visual tree se **feature importance aur decision rules samajh aate hain** — interview + real ML dono mein kaam aata hai.

---

### **Hour 3 Optional: Feature Importance**

```python
import pandas as pd

feat_imp = pd.Series(tree_model.feature_importances_, 
                     index=['Age','Fare','Sex','Pclass'])
print(feat_imp.sort_values(ascending=False))
```

* Ye batata hai kaun sa feature sabse zyada survival predict kar raha hai.
* Interview mein favorite topic ✅

---

### **Mini Practice (Must Do)**

* Change `max_depth=5` aur dekho accuracy + overfitting
* Try `min_samples_split=4` → control tree growth
* Predict on single passenger manually:

```python
sample = X_test[0].reshape(1,-1)
print(tree_model.predict(sample))
```

---

### ❌ **Common Mistakes**

* Unlimited depth → overfitting ❌
* Ignore feature importance ❌
* Evaluate only accuracy ❌

---

### ✅ **Day 5 Takeaways**

1. Decision Tree = **visual + intuitive model**
2. Max depth & min samples → control overfitting
3. Feature importance = ML understanding
4. Confusion matrix = proper evaluation