import random

rand_list = []

for i in range(3):
    inner_list = []
    for j in range(5):
        inner_list.append(random.randint(1, 100))
    rand_list.append(inner_list)

print(rand_list)

