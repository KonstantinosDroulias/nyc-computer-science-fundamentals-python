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
    print(gamedata[data[pc]])
    
    
    
    """
    #If in dictionary
        #grab score to display
if username in gamedata[usernames]:
    print(gamedata['user_score'])
    #esle create new user and give 0 score and computer score
else:
    gamedata.append[username,00:00:00,0,0]"""