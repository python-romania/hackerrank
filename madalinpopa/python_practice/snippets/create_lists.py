# Exemple 1: There are 3 different lists
board = [['_'] * 3 for i in range(3)]
board[1][2] = 'X'
print(f'OK: {board}')

# Exemple 2: There are 3 lists with some reference
row = ['_'] * 3
board = []
for i in range(3):
    board.append(row)
board[1][2] = '0'
print(f'Not OK: {board}')