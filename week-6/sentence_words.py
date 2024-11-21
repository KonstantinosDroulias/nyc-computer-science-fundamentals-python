sentence = input("Write a sentence: ")

counter = 0
flag = 'space'

for i in range(len(sentence)):
    if sentence[i] == ' ':
        flag = 'space'
    else:
        if flag == 'space':
            counter += 1
            flag = 'letter'
    
print(counter)