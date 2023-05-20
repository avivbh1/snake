import tkinter as tk

COLOR = "red"
WIDTH_CELL = 20
LENGTH_CELL = 10


def create_snake(window, board):
    # snake is built from list of cordinates (each cordinate contain row and column index)
    snake_cordinates = [[3, 2], [3, 3], [3, 4]]
    snake = {}  # list of all the square objects that snake is on

    for key in board: # key is the index of the square
        #print(board[key])
        if board[key].cordinates in snake_cordinates:
            board[key].snake_stepped()
            snake[key] = board[key]
            #snake.append(board[key])
    print(str(snake) + "sas")
    return snake








