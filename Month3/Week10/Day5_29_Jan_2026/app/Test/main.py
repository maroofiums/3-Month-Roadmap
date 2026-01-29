import requests

url = "http://127.0.0.1:8000/predict"

data = {
    "sepal_length": 6.0,
    "sepal_width": 3.0,
    "petal_length": 4.8,
    "petal_width": 1.8
}

response = requests.post(url, json=data)
print(response.json())
