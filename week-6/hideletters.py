
word = input("Gve a word: ")

secret = word[0]
for i in range(1, len(word)-1):
    secret += '_'
secret += word[-1]

print(secret)

secret2 = word[0] + '_' * (len(word) - 2) + word[-1]
print(secret2)