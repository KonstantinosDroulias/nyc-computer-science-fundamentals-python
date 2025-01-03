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
        score = wins * 100 + wins/(wins + loses) * wins
        scoredata[i] = score
    else: 
        scoredata[i] = 0


items = list(scoredata.items())

n = len(items)
for i in range(n):
    for j in range(0, n - i - 1):
        # Compare values
        if items[j][1] < items[j + 1][1]:  # Descending order
            # Swap the items
            items[j], items[j + 1] = items[j + 1], items[j]

# Convert the sorted list back to a dictionary
sorted_scoredata = dict(items)

# Print the result
for index, i in enumerate(sorted_scoredata):
    print(f"{index + 1} - {i} : {sorted_scoredata[i]}")
