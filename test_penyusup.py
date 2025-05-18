import requests

url = "http://127.0.0.1:8000/"  # Ganti dengan URL aplikasi Anda
for i in range(30):
    response = requests.get(url)
    print(f"Request {i+1} - Status Code: {response.status_code}")
