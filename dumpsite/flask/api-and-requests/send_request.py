import requests

json_data = {
    'name': 'Jasprit Bumrah',
    'country': 'India'
}

headers = {
    'Content-Type': 'application/json'
}

r = requests.post('http://localhost:5000', json=json_data, headers=headers)

print(r.json())