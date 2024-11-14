"""
Todo:
- Create the board
- Create a player variable
- Loop until ???
- Display board
- Prompt current user to play row and col
- Create if statements to check the board space
    - Check for winner / tie
- Else Error
"""


board = [['-'] * 3 for i in range(3)]

player = 'X'

while True:
    for row in range(3):
        for col in range(3):
            print(board[row][col], end=' ')
        print()


print(f"{player} plays")
r = int(input("Row: "))
c = int(input("Col: "))

if board[r][c] == '-':
    board[r][c] = player

    player = 'X' if player == 'O' else player = 'O'

else:
    print("Error: Invalid position")