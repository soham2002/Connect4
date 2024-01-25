import numpy as np
ROW_COUNT = 6
COL_COUNT = 7
def create_board():
    board = np.zeros((ROW_COUNT,COL_COUNT))
    return board

def drop_piece(board,row,col,piece):
    board[row][col] = piece

def is_valid_location(board,col):
    return board[ROW_COUNT-1][col]== 0

def get_next_open_row(board,col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))

def winning_move(board, piece):
    #HorizontalCheck
    for c in range(COL_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] ==piece and board[r][c+2]==piece and board[r][c+3]==piece:
                return True
    #VerticalCheck
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] ==piece and  board[r+2][c]==piece and board[r+3][c]==piece:
                return True
    #CheckPositiveDiagonal/
    for c in range(COL_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] ==piece and board[r+2][c+2]==piece and board[r+3][c+3]==piece:
                return True
    #CheckNegativeDiagonal\
    for c in range(COL_COUNT-3):
        for r in range(3,ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] ==piece and board[r-2][c+2]==piece and board[r-3][c+3]==piece:
                return True   

board = create_board()
print_board(board)
game_over = False
turn = 0

while not game_over:
    # Asking Player 1 for Input
    if turn == 0:
        col = int(input("Player 1 Make your Selection (0-6)"))

        if is_valid_location(board,col):
            row = get_next_open_row(board,col)
            drop_piece(board,row,col,1)
        
        if winning_move(board,1):
            print("\n \t PLAYER 1 WINS!!!\t \n")
            game_over = True;
    # Asking Player2 for Input
    else:
        col = int(input("Player 2 Make  your Selection (0-6)"))
        
        if is_valid_location(board,col):
            row = get_next_open_row(board,col)
            drop_piece(board,row,col,2)
        
        if winning_move(board,1):
            print("\n \t PLAYER 2 WINS!!!\t \n")
            game_over = True;
  
    print_board(board)
    turn +=1
    turn %=2