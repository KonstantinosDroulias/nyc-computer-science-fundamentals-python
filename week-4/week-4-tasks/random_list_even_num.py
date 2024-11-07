import random

number_list = []
for i in range(20):
    number_list.append(random.randint(1, 100))

even_num = 1
for number in number_list:
    if number % 2 == 0:
        even_num += 1

if even_num != 0:
    print(f"Your Random list {number_list} has {even_num} even numbers")
else:
    print(f"Your Random list {number_list} does not have any even numbers")