import requests

baseUrl = "https://dummyjson.com/"
quotes = "quotes/random"

response = requests.get(baseUrl+quotes)
print(response.status_code)
if response.status_code == 200:
    data = response.json()
elif response.status_code == 400:
    print(f"Bad request, check your request syntax")
elif response.status_code == 500:
    print(f"Server error, chill out it's not your fault, you tired.")
else:
    print(f"Another error {response.status_code}")

print(data["quote"])