import random

"""
Todo
- Generate Random Word
- Loop
- Display Secret
- Ask user for letter
- Update correct or wrong
- Construct secret
- if statemetns
"""

wordlist = ['table',
            'desk',
            'backpack',
            'chair',
            'monitor']

randomword = random.choice(wordlist)
print(randomword)

secret = randomword[0]
for i in range(1, len(randomword)-1):
    secret += '_'
secret += randomword[-1]

correct = []
wrong = []
while True:
    print(secret)
    
    letter = input('Type a letter: ')
    if letter in correct or letter in wrong:
        pass
    else:
        if letter in randomword:
            correct.append(letter)
        else:
            wrong.append(letter)
    
    secret = randomword[0]
    for i in range(1, len(randomword)-1):
        if randomword[i] in correct:
            secret += randomword[i]
        else:
            secret += "_"   
    secret += randomword[-1]
    
    if secret == randomword:
        print(secret)
        print('FOUND!')
        break
    elif len(wrong) == 6:
        print('HANGED')
        break