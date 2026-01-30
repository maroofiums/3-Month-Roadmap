
# Month3 Week10 Day6 -- Titanic Survival Prediction API

A **FastAPI application** that predicts whether a passenger would survive the Titanic disaster based on features like age, sex, class, fare, and family information.  
The ML model is trained using **Random Forest** on the Titanic dataset (Seaborn version) and saved as a `.pkl` file.

---

## 📂 Project Structure

```

project/
├─ app/
│   ├─ **init**.py
│   ├─ main.py            # FastAPI app
│   ├─ models.py          # Pydantic input/output schemas
│   └─ Model/             # Folder containing saved ML models
│       ├─ titanic_model.pkl
│       └─ titanic_features.pkl
└─ README.md

````

---

## ⚡ Features

- Predict survival of Titanic passengers
- Easy-to-use API endpoint `/predict`
- Input validation using **Pydantic**
- Handles numerical & categorical features
- Fast, ready-to-deploy ML model using `.pkl` file

---

## 🛠 Requirements

- Python >= 3.9
- FastAPI
- Uvicorn
- Pandas
- Scikit-learn
- Pickle (built-in)

Install dependencies:
```bash
pip install fastapi uvicorn pandas scikit-learn
````

---

## 🚀 How to Run

1. Clone the repo:

```bash
git clone <your-repo-url>
cd project
```

2. Run FastAPI app:

```bash
uvicorn app.main:app --reload
```

3. Open the API docs at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📦 API Usage

**POST** `/predict`

**Input JSON Example:**

```json
{
  "pclass": 3,
  "sex": 1,
  "age": 29,
  "sibsp": 0,
  "parch": 0,
  "fare": 7.25,
  "embarked_Q": 0,
  "embarked_S": 1
}
```

**Output JSON Example:**

```json
{
  "survived": 0
}
```

---

## 🔧 Notes

* `.pkl` model and features must be in `app/Model/`
* Make sure input JSON matches the feature order in `titanic_features.pkl`
* Can be extended to **handle raw categorical inputs** (`sex="male"`, `embarked="S"`) by adding preprocessing in `main.py`

---