import requests

url = "https://pokeapi.co/api/v2/pokemon/?offset=140&limit=5"

""" variables can be limit, name, offset, move, etc. Not just specific pokemon 
but generally look up your variables so you can use the data effectively"""

# Status Code: 200: (ok) 404: (not-found), 403: (forbidden), 401: (unauth), 400:(bad request) status code cats/dogs
# 500s server issue
# 200s generally okay
# Create - 201, Delete - 204, read - 200, update - 201,200
# 300s redirection
# 400s your issue

result = requests.get(url)
less_res = result.json()["results"]

for i in less_res:
    print(i["name"])

poke_name = "errorpls!"

name_url = f"https://pokeapi.co/api/v2/pokemon/{poke_name}"

response = requests.get(name_url)

if response.status_code == 200:
    data = response.json()
elif response.status_code == 404:
    print(f"{poke_name} not found")
elif response.status_code == 400:
    print(f"Bad request, check your request syntax")
elif response.status_code == 500:
    print(f"Server error, chill out it's not your fault, you tired.")
else:
    print(f"Another error {response.status_code}")