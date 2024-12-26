students = ['John Doe', 'Mary Smith', 'Andrew Green', 'Lisa Tomas',
'Mike Smith', 'Alex Green']

usernames = []

#for i in range(0, len(students)):
for i in students:
    #print(i)
    username = i[0]
    flag = False
    for j in i:
        if j == ' ':
            flag = True
        if flag == True and j != ' ':
            username += j
        
    if username in usernames:
        username += '1'
        usernames.append(username.lower())
    else:
        usernames.append(username.lower())

print(usernames)