import requests

url = 'http://127.0.0.1:5000/tasks'
data = {"titulo": "Estudar Python"}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())
