import requests
response = requests.get("http://api.open-notify.org/astros.json")
print(response.json())
for i in response.json()['people']:
    print(i['craft'])
