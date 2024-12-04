#!/usr/bin/env python3

"""
Jonathan Visona
CPSC6210-02-2024FA
Assignment 4
tic_tac_toe.py
"""

# This constructs a multi-dimensional array with an inner and outer comprehension
grid = [[' ' for _ in range(3)] for _ in range(3)] # note the anonymous variable _

def display_grid():
    print()
    print("+-+-+-+-+-+-+")
    for row in grid:
        print("|", end="")
        for column in row:
            print(" " + column + " |", end="")
        print()
        print("+-+-+-+-+-+-+")
    print()

def take_turn( turn ):
    while True:
        mark = "X" if turn%2 == 1 else "O"
        print( f"{turn=} {mark=}")
        while True:
            row = int(input("Pick a row (1, 2, 3): ")) - 1
            column = int(input("Pick a column (1, 2, 3): ")) - 1
            if( ( row==0 or row==1 or row==2 ) and ( column==0 or column==1 or column==2 ) ):
               break
        if grid[row][column] == ' ':
            grid[row][column] = mark
            return
        else:
            print(f"{grid[row][column]} is already taken. Try again.")

def check_win( turn ):
    game_is_over = False
    if turn == 9:
        print("It's a tie!")
        game_is_over = True
    elif check_for_winner() == "X":
        display_grid()
        print( "X wins!" )
        game_is_over = True
    elif check_for_winner() == "O":
        display_grid()
        print( "O wins!" )
        game_is_over = True
    return game_is_over

def check_for_winner():
    # rows
    for x in range(3):
        if grid[x][0] == grid[x][1] and grid[x][1] == grid[x][2]:
            return grid[x][0]
    # columns
    for y in range(3):
        if grid[0][y] == grid[1][y] and grid[1][y] == grid[2][y]:
            return grid[0][y]
    # major diagonal
    if grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2]:
        return grid[0][0]
    # minor diagonal
    if grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0]:
        return grid[2][0]
    # no winner yet
    return " "

def main():
    game_is_over = False
    turn = 1
    print( "\n*** TIC TAC TOE ***" )
    while not game_is_over:
        display_grid()
        take_turn( turn )
        game_is_over = check_win( turn )
        turn += 1

if __name__ == "__main__":
    main()