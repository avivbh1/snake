import tkinter as tk

COLOR = "red"
WIDTH_CELL = 20
LENGTH_CELL = 10


def show_snake_after_move(window, board, snake):
    # snake is a dictionary of all the squares is on and their index
    for index in board:
        if board[index] == list(snake.values())[-1]:
            board[index].snake_stepped()
        #if board[index] in list(snake.values()):
        #    board[index].snake_stepped()

"""    snake_label = tk.Label(bg=COLOR, padx=WIDTH_CELL, pady=LENGTH_CELL)
    snake_label.grid(row=snake[cell][0], column=snake[cell][1])"""



