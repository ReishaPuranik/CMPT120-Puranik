# CMPT 120 Intro to Programming
# Lab #6 – Lists and Error Handling
# Author: Reisha Puranik
# Created: 2019-10-21
symbol = [ " ", "x", "o" ]
def printRow(row):
    line = "| "
    for col in row:
        line = line + symbol[col] + " | "
    print(line)
    
def printBoard(board):
    print("+-----------+")
    for row in board:
        printRow(row)
        print("+-----------+")
    pass
def markBoard(board, row, col, player):
    if board[row][col] == 0:
        board[row][col] = player
        return True
    else:
        return False
    pass
def getPlayerMove():
    row = int(input("Enter row number: "))
    col = int(input("Enter column number: ")) 
    return (row, col) 

def hasBlanks(board):
    for row in board:
        for col in row:
            if col == 0:
                return True
    return False
def main():
    board = [[0,0,0],
             [0,0,0],
             [0,0,0]]
    player = 1
    while hasBlanks(board):
        printBoard(board)
        row,col = getPlayerMove()
        if not markBoard(board,row,col,player):
            print("Choose another position")
        else:
            player = player % 2 + 1 
    printBoard(board)
        
main()
