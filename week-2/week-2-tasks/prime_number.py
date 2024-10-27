user_input = int(input("Type a number to check if it is prime: "))

result = []

for i in range(2, user_input):
    division = user_input % i
    if division != 0:
        result.append(True)
    else:
        result.append(False)


if all(result):
    print(f"Brilliant, {user_input} is a prime number")
else:
    print(f"Ohh, {user_input} is not a prime number")