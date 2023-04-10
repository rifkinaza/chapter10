import requests

api_key = '10d8cd54-f6d7-4929-8f49-74fd63acab1f'
word = 'tomato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions :
    print(definition)