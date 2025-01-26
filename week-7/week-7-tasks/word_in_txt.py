word = input("Search: ")
word = word.strip().lower()

file = open('story.txt', 'r')

count = 0
for line in file:
    #print(line)
    line = line.strip().lower()
    
    if word == line:
        count += 1

if count > 0:
    print(f"Your word exists {count} times")
else:
    print("Your word does not exist in the file")