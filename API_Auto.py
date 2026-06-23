import requests

response = requests.get("https://api.github.com")
print(response.status_code)

if response.status_code == 200:
    print("API is responding successfully!")
else:    print("API is not responding as expected.")  

#if we want to check the response content, we can do so by printing the response text or JSON data.
print(response.text)  # Print the raw response text
print(response.json())  # Print the response as JSON data