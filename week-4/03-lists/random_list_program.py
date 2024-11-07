import random

size = int(input("Give list length: "))

data = []
for i in range(size):
    data.append(random.randint(1, 100))
    print(data[i], end=' ')

print()

x = int(input("Give a number to check if it exists in the list: "))
v = False
for i in range(len(data)):
    if x == data[i]:
        v = True
        print("Found your Number")
        break
    
if v != True:
    print('Your Number was not found')

average = sum(data)/len(data)
print(f'Average of list: {average}')