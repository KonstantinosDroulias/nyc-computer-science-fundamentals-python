import random

random_list = []

for i in range(100):
    random_list.append(random.randint(1, 50))

user_num = int(input('Type a number to check if and how many times it exists in the list: '))

counter = 0
for item in random_list:
    if user_num == item:
        counter += 1

print(random_list)
if counter != 0:
    print(f"{user_num} is {counter} times in the list")
else:
    print(f"{user_num} does not exist in the list")