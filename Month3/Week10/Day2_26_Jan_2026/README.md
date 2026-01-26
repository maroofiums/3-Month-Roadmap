# Month3 - Week10 - Day 2
# Customer Churn Prediction API

This project provides a **FastAPI backend** to predict customer churn using a pre-trained machine learning model.  
It is designed for easy integration with dashboards, web apps, or other services.

---

## 🚀 Features

- Predicts whether a customer will churn (`churn=0` or `churn=1`)
- Returns **probability of churn** for threshold tuning
- Input validation using **Pydantic schemas**
- Preprocessing included (Label Encoding, feature selection, etc.)
- Uses top features identified via Random Forest
- Supports **multiple models**; best model selected based on **recall**

---

## 📁 Project Structure

```

churn_api/
├─ app/
│  ├─ **init**.py
│  ├─ main.py           # FastAPI app & endpoints
│  ├─ model.py          # Model loading & preprocessing
│  └─ schemas.py        # Input validation
├─ top_features.pkl      # Selected top features
├─ churn_model.pkl       # Trained ML model
├─ label_encoder.pkl     # Label Encoder object
├─ requirements.txt      # Python dependencies
└─ README.md

````

---

## ⚙️ Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd churn_api
````

2. Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the API server:

```bash
uvicorn app.main:app --reload
```

5. Open your browser and check:

```
http://127.0.0.1:8000/docs
```

You will see **Swagger UI** for testing endpoints.

---

## 📝 API Endpoints

### 1. Health Check

```
GET /
```

**Response:**

```json
{
  "message": "Customer Churn Prediction API is running!"
}
```

---

### 2. Predict Churn

```
POST /predict
```

**Request JSON Example:**

```json
{
  "tenure": 12,
  "MonthlyCharges": 70.35,
  "TotalCharges": 845.5,
  "Contract": "Month-to-month",
  "PaymentMethod": "Electronic check",
  "OnlineSecurity": "No",
  "TechSupport": "No",
  "InternetService": "DSL",
  "OnlineBackup": "Yes",
  "PaperlessBilling": "Yes",
  "MultipleLines": "No",
  "gender": "Female",
  "DeviceProtection": "Yes",
  "Partner": "No",
  "Dependents": "No",
  "StreamingMovies": "No",
  "StreamingTV": "Yes"
}
```

**Response Example:**

```json
{
  "churn": 1,
  "churn_probability": 0.732
}
```

* `churn`: 1 = customer likely to churn, 0 = customer unlikely to churn
* `churn_probability`: probability of churn (0–1), useful for threshold tuning

---

## 🔧 Preprocessing

* Label encoding for binary and low-cardinality categorical features
* One-hot encoding for high-cardinality categorical features
* Outlier clipping using **IQR method**
* Feature selection using **Random Forest importance**
* Top features saved in `top_features.pkl`
* Label encoder saved in `label_encoder.pkl`

---

## 📈 Model Details

* Model type: **Naive Bayes** (selected based on **recall**)
* Achieved metrics on test set:

  * Accuracy: 0.747
  * Precision: 0.516
  * Recall: 0.733
  * F1-Score: 0.606
* Saved as `churn_model.pkl` for deployment

---

## 📦 Usage

1. Send a POST request with customer data to `/predict`
2. Use `churn_probability` to adjust business decision thresholds
3. Integrate with **Streamlit dashboards** or **web apps**

---
