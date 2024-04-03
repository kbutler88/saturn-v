import requests, json
from datetime import datetime

r = requests.get('https://randomuser.me/api')

parsed_data = json.loads(r.text)

# Print structured JSON data
#print(json.dumps(parsed_data, indent=4))
#print()

gender = parsed_data['results'][0]['gender']
name = parsed_data['results'][0]['name']['title'] + '. ' + parsed_data['results'][0]['name']['first'] + ' ' + parsed_data['results'][0]['name']['last']
age = parsed_data['results'][0]['dob']['age']
dob = parsed_data['results'][0]['dob']['date']
# Split the date from the time
parsed_dob = dob.split("T")
# Just for fun, format the date into a new format
# Use the "string parse time" function to feed the original format
converted_dob = datetime.strptime(parsed_dob[0], "%Y-%m-%d")
# Split the original format to each individual date component
#new_dob = parsed_dob[0].split("-")
# Convert the numeric month to the month name
#if new_dob[1] == '01':
#    new_dob[1] = "January"
#if new_dob[1] == '02':
#    new_dob[1] = "February"
#if new_dob[1] == '03':
#    new_dob[1] = "March"
#if new_dob[1] == '04':
#    new_dob[1] = "April"
#if new_dob[1] == '05':
#    new_dob[1] = "May"
#if new_dob[1] == '06':
#    new_dob[1] = "June"
#if new_dob[1] == '07':
#    new_dob[1] = "July"
#if new_dob[1] == '08':
#    new_dob[1] = "August"
#if new_dob[1] == '09':
#    new_dob[1] = "September"
#if new_dob[1] == '10':
#    new_dob[1] = "October"
#if new_dob[1] == '11':
#    new_dob[1] = "November"
#if new_dob[1] == '12':
#    new_dob[1] = "December"

print(f'Gender: {gender}')
print(f'Name: {name}')
print(f'Age: {age}')
# New dob date conversion
print(f'DoB: {converted_dob.strftime("%B %d, %Y")}')
# Old date conversion
#print(f'DoB: {new_dob[1]} {new_dob[2]}, {new_dob[0]}')
