# Battleship
board = []

for i in range(5):
	board.append(["O"] * 5)

def print_board(board_in):
  for row in board_in:
    print row
    
print_board(board)