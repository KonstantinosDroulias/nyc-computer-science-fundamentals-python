user_input = input("Search: ")

counter = 0
with open ('story.txt', 'r') as st:
    if user_input in st:
        counter =+ 1

if counter > 0:
    print(f"The word {user_input} is {counter} times in the story.txt")
else:
    print(f"Sorry, {user_input} is not in the story.txt file")
    
