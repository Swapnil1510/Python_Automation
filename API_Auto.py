import requests

response = requests.get("https://api.github.com")
print(response.status_code)

if response.status_code == 200:
    print("API is responding successfully!")
else:    print("API is not responding as expected.")