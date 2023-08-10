 

board = [3, 2, 1, 6, 5, 4, 7, 8, 9]
print(board)
def draw_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-------------")
draw_board(board)

board.sort(key=5, reverse=True)
print()