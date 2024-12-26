username = input("Enter Your Username: ")
    #Open csv and manage it in a dictionarry 
gamedata = {}

with open('gamedata.csv', 'r') as gd:
    lines = gd.readlines()
    #print(lines)
    headers = lines[0].strip().split(',')
    """
    for line in lines[1:]:
        values = line.strip().split(',')
        for i in range(len(headers)):
            #print(headers[i])
            #print(values[i])
            #print(i)
            if i == 0:    
                usernames = values[i]
                #print(f"Usernames {usernames}")
            if i > 0:    
                data.append({headers[i]: values[i]})
                #print(f"Data {data}")
                
        row = {usernames : data}
        #print(f"Row {row}")
        gamedata.append(row)

print(gamedata)"""

    for line in lines[1:]:
        print(lines)
        values = line.strip().split(',')
        print(values)
        data = {}
        for i in range(len(headers)):
            print(i)
            if i == 0:
                username = values[0]
            else:
                data[headers[i]] = values[i]
                print(data)
            gamedata[username] = data
            
        print(gamedata)
