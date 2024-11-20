def print_characters(ch, n, e):
     for i in range(n):
          print(ch, end=e)

user_input = int(input("Type a number for the height of the tree: "))
spaces = user_input // 2
asterisks = 1

while asterisks <= user_input:
    print_characters(' ', spaces, ' ')
    print_characters('*', asterisks, ' ')

    print()

    spaces -= 1

    asterisks += 2

spaces += 1
asterisks -= 2

while asterisks >= 1:
    spaces += 1
    asterisks -= 2
    
    print_characters(' ', spaces, ' ')
    print_characters('*', asterisks, ' ')

    print()
