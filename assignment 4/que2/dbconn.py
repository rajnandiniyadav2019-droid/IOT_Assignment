import requests

data = {
    "light": "ON",
    "fan": "OFF",
    "temperature": 29
}

r = requests.post(
    "http://127.0.0.1:5000/update",
    data=data
)

print(r.text)
