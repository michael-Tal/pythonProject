import requests

response = requests.post("http://127.0.0.1:5001/whatismyname")
expexted = "saved new car"
actual = response.text
assert expexted == actual
assert response.status_code == 200