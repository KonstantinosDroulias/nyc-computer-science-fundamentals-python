"""I throught my code in chatgpt after not being able to get the extra number at the end and get code that was much smarter than mine so I wanted to keep it here"""

students = ['John Doe', 'Mary Smith', 'Andrew Green', 'Lisa Tomas',
            'Mike Smith', 'Alex Green']

usernames = []

for student in students:
    # Split the student's full name into first and last name
    first, last = student.split(' ')
    # Construct the initial username using the first letter of the first name and the last name
    username = first[0] + last
    
    # Check for duplicates and append a number if necessary
    if username.lower() in usernames:
        count = 1
        new_username = username + str(count)
        while new_username.lower() in usernames:
            count += 1
            new_username = username + str(count)
        username = new_username
    
    # Add the username to the list (lowercase to ensure consistency)
    usernames.append(username.lower())

print(usernames)
