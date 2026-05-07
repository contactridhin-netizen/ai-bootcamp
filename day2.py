import requests

url = "https://api.github.com/users/contactridhin-netizen"

response = requests.get(url)
data = response.json()

print("Username:", data["login"])
print("Public repos:", data["public_repos"])

print(response)
print(response.text)
print(data)