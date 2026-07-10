import requests

data = {
    "temperature": 30,
    "intensity": 500
}

r = requests.post("http://127.0.0.1:5000/update", data=data)
print(r.text)
