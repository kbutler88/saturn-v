import requests, json

r = requests.get('https://randomuser.me/api')

parsed_data = json.loads(r.text)

print(json.dumps(parsed_data, indent=4))

print()

gender = parsed_data['results'][0]['gender']
name = parsed_data['results'][0]['name']['title'] + '. ' + parsed_data['results'][0]['name']['first'] + ' ' + parsed_data['results'][0]['name']['last']
print(f'Gender: {gender}')
print(f'Name: {name}')
