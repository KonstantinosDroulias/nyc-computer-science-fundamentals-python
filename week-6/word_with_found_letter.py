
word = 'backpack'
correct = ['a', 'p', 'k']

secret = word[0]
for i in range(1, len(word)-1):
    if word[i] in correct:
        secret += word[i]
    else:
        secret += "_"
secret += word[-1]
print(secret)