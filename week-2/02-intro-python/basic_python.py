print('Hello World!')

# language is a variable
language = input("Wich programming langauge are you learning? ")
language = language.strip()
print(f"Oh, {language}! This is great!")


if language == 'Python':
    print("Good choice")

elif language == 'Java':
    print("Good, but don't forget Python, too")

else:
    print("You could also try Python")

