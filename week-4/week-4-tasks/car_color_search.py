
colors = ["Red", "Green", "White", "Blue", "Violet"]

v = True
while v == True:
    user_input = input("Select your prefered color: ")
    user_input_lower = user_input.lower()

    colors_lower = []
    for color in colors:
        colors_lower.append(color.lower())

    if user_input_lower in colors_lower:
        print("The color you've selected is available")
        v = False
    else:
        print(f"{user_input} is not available.\n-The available colors are:")
        for i in range(len(colors)):
            print(f"{colors[i]},", end=' ')
        print('\nProgramm is restarting')

    