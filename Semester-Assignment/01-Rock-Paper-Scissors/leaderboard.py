gamedata = {}

datafile = 'gamedata.csv'

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
            
# Code above was copied from the main game file

scoredata = {}

for i in gamedata:
    if i == 'pc':
        continue
    wins = int(gamedata[i]['user_score'])
    loses =int(gamedata[i]['computer_score'])
    # I set each win to be worth 100 points
    if wins != 0:
        score = wins * 100 + wins/(wins + loses) * wins #Score is win points * 
        scoredata[i] = score
    else: 
        scoredata[i] = 0


sorted_scoredata = dict(sorted(scoredata.items(), key=lambda x: x[1], reverse=True))

for index, (user, score) in enumerate(sorted_scoredata.items(), start=1):
    print(f"{index} - {user} : {score}")
