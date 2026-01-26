
# **Month3 Week9 Day7 -- Customer Churn Prediction – End-to-End ML Pipeline**

## **Project Overview**

This project builds a **production-ready machine learning pipeline** to predict **customer churn** using structured customer data.
The notebook demonstrates the **complete workflow from raw data to deployable model artifacts**, combining EDA, preprocessing, feature engineering, model selection, and deployment readiness.

---

## **Key Features**

1. **Data Loading & Cleaning**

   * Handles missing values and invalid data
   * Converts data types for model compatibility
   * Drops irrelevant identifiers (`customerID`)

2. **Exploratory Data Analysis (EDA)**

   * Visualizes numerical distributions, skewness, and outliers
   * Plots categorical class distributions for imbalance detection
   * Correlation heatmap for feature insights

3. **Feature Encoding & Boolean Handling**

   * Hybrid approach: Label Encoding for low-cardinality features, One-Hot Encoding for high-cardinality features
   * Boolean columns converted to numeric (0/1)

4. **Outlier Treatment**

   * Capping using the Interquartile Range (IQR) method
   * Preserves dataset size while mitigating extreme values

5. **Feature Selection**

   * Uses Random Forest to identify important features
   * Retains only features with importance > 0.01
   * Reduces dimensionality and improves generalization

6. **Model Training & Hyperparameter Tuning**

   * Evaluates multiple classifiers: Logistic Regression, KNN, Decision Tree, Naive Bayes, Random Forest, Gradient Boosting
   * Hyperparameter tuning using `GridSearchCV` with cross-validation
   * Best model selected based on **recall** score

7. **Model Evaluation**

   * Accuracy, Precision, Recall, F1-Score metrics
   * Confusion matrix visualization for detailed prediction analysis

8. **Exporting Artifacts for Deployment**

   * Saves trained model (`churn_model.pkl`)
   * Saves selected features (`top_features.pkl`)
   * Saves LabelEncoder for categorical features (`label_encoder.pkl`)
   * Ready to integrate with **Streamlit dashboards** or **FastAPI services**

---

## **Dataset**

* The dataset contains structured customer data with features such as:

  * Demographics (e.g., gender, senior citizen)
  * Account information (tenure, contract type, monthly charges)
  * Service usage metrics
* Target variable: `Churn` (1 = churned, 0 = retained)

**Note:** Dataset used in this notebook is a cleaned version for demonstration purposes.

---

## **Technologies & Libraries**

* Python 3.x
* Pandas & NumPy – data manipulation
* Matplotlib & Seaborn – visualization
* Scikit-learn – preprocessing, modeling, and evaluation
* Joblib – saving model artifacts

---

## **Project Workflow**

1. **Load Dataset** → Inspect and clean data
2. **EDA** → Visualize numerical & categorical features
3. **Preprocessing** → Encode categorical variables, handle booleans, treat outliers
4. **Feature Selection** → Reduce dimensionality using Random Forest
5. **Train-Test Split** → 80/20 stratified split
6. **Model Training & Tuning** → GridSearchCV on multiple classifiers
7. **Evaluation** → Metrics + Confusion matrix
8. **Export** → Save model and preprocessing artifacts for deployment

---

## **Conclusion**

This notebook provides a **complete, end-to-end ML pipeline** for customer churn prediction.
It can be extended for:

* **Other classification problems** with tabular data
* Integration with **APIs** (FastAPI) or **dashboard apps** (Streamlit)
* Experimenting with **advanced feature selection** or **ensemble methods**
