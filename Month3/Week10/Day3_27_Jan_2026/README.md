# Month3 Week10 Day3 Customer Churn Prediction API

A **production-ready FastAPI backend** for predicting customer churn using a pre-trained machine learning model.
The API is designed for seamless integration with dashboards, web applications, and data-driven decision systems.

---

## Overview

This service predicts whether a customer is likely to churn and returns both:

* A **binary churn prediction**
* A **churn probability score** for threshold-based business decisions

The API follows clean architecture principles, includes preprocessing logic, and supports **asynchronous endpoints** for improved scalability.

---

## Key Features

* REST API built with **FastAPI**
* Asynchronous endpoints for high concurrency
* Churn prediction (`0 = No`, `1 = Yes`)
* Probability-based output for decision tuning
* Input validation using **Pydantic**
* Preprocessing pipeline included
* Feature selection using **Random Forest importance**
* Model selection based on **Recall optimization**
* Swagger UI for interactive testing

---

## Tech Stack

* Python
* FastAPI
* Scikit-learn
* Pydantic
* Uvicorn
* Pickle (model persistence)

---

## Project Structure

```
churn_api/
├─ app/
│  ├─ __init__.py
│  ├─ main.py          # FastAPI app & async endpoints
│  ├─ model.py         # Model loading & prediction logic
│  └─ schemas.py       # Pydantic request schemas
├─ churn_model.pkl      # Trained ML model
├─ top_features.pkl     # Selected top features
├─ label_encoder.pkl    # Label encoder
├─ requirements.txt
└─ README.md
```

---

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd churn_api
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the API Server

```bash
uvicorn app.main:app --reload
```

### 5. Access API Documentation

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Health Check

**GET /**

**Response**

```json
{
  "message": "Customer Churn Prediction API is running"
}
```

---

### Predict Customer Churn

**POST /predict**

#### Request Body

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

#### Response

```json
{
  "churn": 1,
  "churn_probability": 0.732
}
```

---

## Preprocessing Pipeline

* Label encoding for binary and low-cardinality categorical features
* One-hot encoding for multi-class categorical features
* Outlier handling using **IQR clipping**
* Feature selection via **Random Forest feature importance**
* Selected features persisted in `top_features.pkl`
* Encoders persisted for inference consistency

---

## Model Information

* Algorithm: **Naive Bayes**
* Selection Criteria: **Highest Recall**
* Test Set Performance:

  * Accuracy: 0.747
  * Precision: 0.516
  * Recall: 0.733
  * F1-Score: 0.606

The trained model is stored as `churn_model.pkl` and loaded once at application startup.

---

## Asynchronous API Design (Day 3)

* Endpoints implemented using `async def`
* Enables handling multiple concurrent requests efficiently
* Improves performance under high load
* Suitable for dashboards and real-time systems

> Note: Model inference remains synchronous to ensure stability, while the API layer is asynchronous.

---

## Usage

1. Send customer data to `/predict`
2. Use `churn_probability` for threshold-based actions
3. Integrate with:

   * Streamlit dashboards
   * Web applications
   * CRM or analytics systems

---

## Best Practices Followed

* Model loaded once at startup
* Clean separation of concerns
* Validation at API boundary
* Scalable async architecture
* Production-ready structure

---

## Future Enhancements

* Async database integration (PostgreSQL)
* Background task logging
* Model versioning
* Docker & CI/CD pipeline
* Authentication & rate limiting

---
