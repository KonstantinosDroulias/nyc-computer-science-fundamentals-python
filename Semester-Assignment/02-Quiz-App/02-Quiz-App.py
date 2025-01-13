"""
User Login:
    - CSV File for UserData:
        - Username
        - Password
    - Create User:
        - Store in Dictionary
Quiz:
    - API for questions + answers
        - Show Question and All 4 answers
        - User Selects an answer
"""

import requests
import json
import random

datafile = 'gamedata.csv'
    #Get User name // This part is copy pasted from my previous work on the Rock Paper Scissors Game. Of course with neccesarry changes for the password login
gamedata = {}

#Open csv and manage it in a dictionarry 
with open(datafile, 'r') as gd:
    lines = gd.readlines()
    headers = lines[0].strip().split(',')
    for line in lines[1:]:   
        values = line.strip().split(',')  
        data = {}
        for i in range(len(headers)):  
            if i == 0:
                usernames = values[0]
            else:
                data[headers[i]] = values[i]
                 
            gamedata[usernames] = data
              
print(data, gamedata)
#User Login            
user_account_state = input("'Log In' or 'Create Account': ")
user_account_state = user_account_state.lower().replace(" ", "")
while user_account_state != 'login' and user_account_state != 'createaccount':
    print('There was a Typo or Invalid Input')
    user_account_state = input("Type 'Log In' If you already have an account or 'Create Account' for new users: ")
    user_account_state = user_account_state.lower().replace(" ", "")
    if user_account_state == 'login' or user_account_state == 'createaccount':
        break

flag = False
while flag != True:
    username = input("Enter Your Username: ")
    password = input("Enter Your Password: ")
        
    #if user_account_state 
    if user_account_state == 'login':
        if username in gamedata:
            if gamedata[username]['password'] == password:
                flag = True     
            #print(f"Your current score is {gamedata[username]['user_score']}")
            else:
                print('Incorrect Login Credentians')
            #esle create new user and give 0 score and computer score
        else:
            #ew_user_data = {0,0,0}
            print('User does not exist')
    else:
        if username not in gamedata:
            gamedata[username] = {'password': password, 'win_score': 0, 'lose_score': 0}
            print('Your User has been created')
            flag = True
        else:
            print(f'{username}, already exists')    
            
print('Succesfull Login')

url = "https://opentdb.com/api.php?amount=10"

response = requests.get(url)

api_data = response.json()

questions = api_data['results']

for i, question in enumerate(questions):
        print(f"Question {i + 1}: {question['question']}")
        print("Choices:")
        options = []
        options = question['incorrect_answers'] + [question['correct_answer']]
        random.shuffle(options)
        print(options)
        for j, option in enumerate(options):
            print(f"{j + 1}. {option}")
            
        answer = int(input('Type the number with the answer you want to choose: '))
        
        if options[int(answer) - 1] == question['correct_answer']:
            print("Brilliant, your answer was correct!")
            # Convert win_score to int and increment
            gamedata[username]['win_score'] = int(gamedata[username].get('win_score', 0)) + 1
        else:
            print(f"Your answer was incorrect. The correct answer was {question['correct_answer']}\nBetter luck next time!")
            # Convert lose_score to int and increment
            gamedata[username]['lose_score'] = int(gamedata[username].get('lose_score', 0)) + 1

with open(datafile, "w") as file:
    file.write("username,password,win_score,lose_score\n")
    
    for username, stats in gamedata.items():
        win_score = stats['win_score']
        lose_score = stats['lose_score']
        
        line = f"{username},{password},{win_score},{lose_score}\n"
        
        file.write(line)