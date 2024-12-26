"""
Rquirments:
- User Login
    - Name Entry // done
- Game Functionality 
    - User selects // done
    - Pc random select // done
    - Win/Draw // done
    - Scoreboard // For user Victory must win 10 rounds in a single game
    - 5 top users
- Files
    - Main Game File
    - scoreboard.csv
        - username
        - datetime
        - user_score
        - computer_score
        - win_rate
- Extra -//- Not Needed for the assigment
    - Gui app
    - Exit Button // Notify user score won't be updated if he leaves too soon
    - 
"""
import random
import datetime #Found in w3schools.com/python/python_datetime.asp

#Todo
    #Get User name
username = input("Enter Your Username: ")
    #Open csv and manage it in a dictionarry 
gamedata = {}

with open('gamedata.csv', 'r') as gd:
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
        
    #If in dictionary
        #grab score to display
if username in gamedata[usernames]:
    print(gamedata['user_score'])
    #esle create new user and give 0 score and computer score
else:
    gamedata.append[username,00:00:00,0,0]
    
    
#Loop till either pc or player reaches 10 wins
user_score = 0
pc_score = 0
weapones = ['Rock', 'Paper', 'Scissors']
while user_score <= 10 or pc_score <=10:
    #Have user select weapon
    for index, i in enumerate(weapones):
        print(f"{index + 1}. {i}")
    
    user_choice = int(input('Type 1-3 to select weaopn: '))
    user_choice -= 1
    #Get pc to randomly select
    pc_choice = random.randint(0, 2)
    #Compere with if statement and keep temp_score
    if user_choice == pc_choice:
        print(f"You({username}), drawed {weapones[user_choice]} and PC drawed {pc_choice}")
        print(f"Intresting... It's a DRAW.")
        
        #Compare 01
    elif weapones[user_choice] == 'Rock':
        if weapones[pc_choice] == 'Paper':
            print(f"You({username}), drawed {weapones[user_choice]} and PC drawed {pc_choice}")
            print(f"Whooops... Paper is stronger than rock. PC won +1 point")
            pc_score += 1
        
        elif weapones[pc_choice] == 'Scissors':
            print(f"You({username}), drawed {weapones[user_choice]} and PC drawed {pc_choice}")
            print(f"Awesome. Rock is stronger than rock you won +1 point")
            user_score += 1
            
    #Compare 02
    elif weapones[user_choice] == 'Paper':
        if weapones[pc_choice] == 'Scissors':
            print(f"You({username}), drawed {weapones[user_choice]} and PC drawed {pc_choice}")
            print(f"Whooops... Paper is stronger than rock. PC won +1 point")
            pc_score += 1
        
        elif weapones[pc_choice] == 'Rock':
            print(f"You({username}), drawed {weapones[user_choice]} and PC drawed {pc_choice}")
            print(f"Awesome. Rock is stronger than rock you won +1 point")
            user_score += 1
        
    #Compare 03
    elif weapones[user_choice] == 'Scissors':
        if weapones[pc_choice] == 'Paper':
            print(f"You({username}), drawed {weapones[user_choice]} and PC drawed {pc_choice}")
            print(f"Whooops... Paper is stronger than rock. PC won +1 point")
            pc_score += 1
        
        elif weapones[pc_choice] == 'Rock':
            print(f"You({username}), drawed {weapones[user_choice]} and PC drawed {pc_choice}")
            print(f"Awesome. Rock is stronger than rock you won +1 point")
            user_score += 1

#Update score with 10 points

    
    