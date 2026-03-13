import requests

url = input("Enter URL: ")

response = requests.get(url)

print("Status Code:", response.status_code)
