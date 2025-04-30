import requests

url = 'http://127.0.0.1:5000/tasks/1'
data = {"titulo": "Estudar Flask", "status": "concluida"}

response = requests.put(url, json=data)

print(response.status_code)
print(response.json())
