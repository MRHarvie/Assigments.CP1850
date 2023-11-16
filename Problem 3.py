# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 16:04:01 2023

@author: harv3
"""

def print_board(board):
    for row in range(len(board)):
        print("+---+---+---+")
        print("|", end="")
        for column in range(len(board[row])):
            print(f" {board[row][column]} |", end="")
        print()
    print("+---+---+---+")

def check_winner(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        row = int(input(f"Player {player}, enter row (0, 1, 2): "))
        col = int(input(f"Player {player}, enter column (0, 1, 2): "))

        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
            print("Invalid move. Try again.")
            continue

        board[row][col] = player
        print_board(board)

        winner = check_winner(board)
        if winner:
            print(f"Player {winner} wins!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
