
## **Week 9 (18 Jan – 24 Jan) – ML Basics**

**Goal:** Learn Numpy, Pandas, and basic ML models (Logistic Regression, Decision Tree, KNN) and practice feature engineering.

---

### **Day 1 – Mon (18 Jan) → Numpy Basics**

**Focus:** Arrays, operations, indexing, reshaping

**Tasks:**

* Create arrays: `np.array([1,2,3])`
* Practice indexing & slicing: `arr[0:2]`
* Reshape arrays: `arr.reshape(3,1)`
* Vectorized operations: add, multiply arrays without loops
* Generate random numbers: `np.random.rand(3,3)`

**Mini Exercise:**

```python
import numpy as np

arr = np.array([1,2,3,4,5,6])
arr2d = arr.reshape(2,3)
print("2D Array:\n", arr2d)
print("Sum along axis 0:", arr2d.sum(axis=0))
```

**Tip:** Think of Numpy as the **foundation for ML computations**. Every ML library (sklearn, pytorch) relies on it.

---

### **Day 2 – Tue (19 Jan) → Pandas Basics**

**Focus:** DataFrames, reading datasets, handling missing values

**Tasks:**

* Load dataset: `pd.read_csv('titanic.csv')`
* Inspect: `.head(), .info(), .describe()`
* Handle missing data: `.fillna()`, `.dropna()`
* Select columns & rows: `.loc[]`, `.iloc[]`
* Filter data: `df[df['Age']>30]`

**Mini Exercise:**

```python
import pandas as pd

df = pd.read_csv("titanic.csv")
print(df.head())
df['Age'].fillna(df['Age'].mean(), inplace=True)
print("Missing ages filled.")
```

**Tip:** **Data cleaning** is 70% of ML work. Always check for missing values, duplicates, or incorrect types.

---

### **Day 3 – Wed (20 Jan) → Feature Engineering**

**Focus:** Transform raw data to ML-ready features

**Tasks:**

* Encode categorical variables: `pd.get_dummies()`
* Scale numeric features: `StandardScaler`
* Split dataset: `train_test_split(X, y, test_size=0.2)`
* Handle outliers & normalization

**Mini Exercise:**

```python
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

X = df[['Age','Fare']]
y = df['Survived']
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
print(X_train[:5])
```

**Tip:** Feature engineering is **where ML magic happens**. Good features > fancy models.

---

### **Day 4 – Thu (21 Jan) → Logistic Regression**

**Focus:** Train model, evaluate predictions

**Tasks:**

* Train model: `LogisticRegression()`
* Predict on test data
* Evaluate: accuracy, confusion matrix

**Mini Exercise:**

```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
```

**Tip:** Logistic Regression is the **go-to for binary classification**, like survival prediction in Titanic dataset.

---

### **Day 5 – Fri (22 Jan) → Decision Tree**

**Focus:** Train, visualize, interpret

**Tasks:**

* Use `DecisionTreeClassifier`
* Visualize tree with `plot_tree`
* Experiment with `max_depth` to avoid overfitting

**Mini Exercise:**

```python
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

tree = DecisionTreeClassifier(max_depth=3, random_state=42)
tree.fit(X_train, y_train)
y_pred_tree = tree.predict(X_test)

plt.figure(figsize=(12,6))
plot_tree(tree, feature_names=['Age','Fare'], class_names=['Not Survived','Survived'], filled=True)
plt.show()
```

**Tip:** Decision Trees are intuitive and **easy to visualize**, making them perfect for understanding feature importance.

---

### **Day 6 – Sat (23 Jan) → KNN (K-Nearest Neighbors)**

**Focus:** Distance-based classification

**Tasks:**

* Use `KNeighborsClassifier`
* Try different `n_neighbors`
* Normalize data for better results

**Mini Exercise:**

```python
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)

print("KNN Accuracy:", accuracy_score(y_test, y_pred_knn))
```

**Tip:** KNN works well for small datasets. **Always scale features**, because KNN is distance-based.

---

### **Day 7 – Sun (24 Jan) → Mini ML Project**

**Goal:** Combine everything into a small project

**Tasks:**

* Use Titanic dataset (or Iris)
* Prepare data (clean + encode + scale)
* Train Logistic Regression, Decision Tree, KNN
* Compare their accuracy
* Save best model: `joblib.dump(model,'model.pkl')`

**Mini Exercise:**

```python
import joblib

best_model = tree  # assume Decision Tree performed best
joblib.dump(best_model, "titanic_model.pkl")
print("Model saved for deployment.")
```

**Tip:** This **saved model** will be used next week to **serve ML predictions via FastAPI**.
