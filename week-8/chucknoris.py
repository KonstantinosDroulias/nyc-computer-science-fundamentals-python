import requests
import json as js

url = 'https://api.chucknorris.io/jokes/random'

response = requests.get(url)



data = js.loads(response.text)

print(data['value'])