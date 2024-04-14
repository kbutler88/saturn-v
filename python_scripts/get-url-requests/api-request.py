import requests, json, os
from datetime import datetime

def main():
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
    
    print()
    print('User data:')
    print(f'  Gender: {gender}')
    print(f'  Name: {name}')
    print(f'  Age: {age}')
    # New dob date conversion
    print(f'  DoB: {converted_dob.strftime("%B %d, %Y")}')

    # Add name of user to array for tracking
    all_names.append(name)

def savefile():
    file_name = input('Enter a filename: ')
    if file_name != '':
        with open(file_name, 'w') as wf:
            for name in all_names:
                wf.write(name + '\n')
    else:
        print('ERROR: File name cannot be empty!')

def get_month_name_from_date(dob):
    # Split the original format to each individual date component
    new_dob = dob[0].split("-")
    # Convert the numeric month to the month name
    if new_dob[1] == '01':
        new_dob[1] = "January"
    if new_dob[1] == '02':
        new_dob[1] = "February"
    if new_dob[1] == '03':
        new_dob[1] = "March"
    if new_dob[1] == '04':
        new_dob[1] = "April"
    if new_dob[1] == '05':
        new_dob[1] = "May"
    if new_dob[1] == '06':
        new_dob[1] = "June"
    if new_dob[1] == '07':
        new_dob[1] = "July"
    if new_dob[1] == '08':
        new_dob[1] = "August"
    if new_dob[1] == '09':
        new_dob[1] = "September"
    if new_dob[1] == '10':
        new_dob[1] = "October"
    if new_dob[1] == '11':
        new_dob[1] = "November"
    if new_dob[1] == '12':
        new_dob[1] = "December"

    # Old date conversion
    print(f'DoB: {new_dob[1]} {new_dob[2]}, {new_dob[0]}')

# Global array to track names of users in session
all_names = []
file_name = ""

while True:
    print()
    print('Press Enter to get a new user')
    print('Type "u" to see the current list of names')
    print('Type "l" to load user info from a file')
    print('Type "s" to save user info to a file')
    response = input('Type "q" to Quit: ')
    if response.lower() == 'u':
        if not all_names:
            print()
            print('No names have been found yet!')
        else:
            print()
            for name in all_names:
                print(name)
    elif response.lower() == 'l':
        loadfile = input('Enter a filename: ')
        print()
        if loadfile == '':
            print('ERROR: No filename provided!')
        elif os.path.exists(loadfile) == False:
            print('ERROR: No such file!')
        else:
            with open(loadfile, 'r') as rf:
                for line in rf:
                    # .stip() removes the line return at the end of the line
                    line = line.strip()
                    all_names.append(line)
    elif response.lower() == 's':
        if not all_names:
            print('No names have been found yet!')
            really_save = input('Are you sure you want to save? (y/n) ')
            if really_save.lower() == 'y':
                savefile()
        else:
            savefile()
    elif response.lower() == 'q':
        break
    elif response == '':
        main()
