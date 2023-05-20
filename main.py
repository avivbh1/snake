import tkinter as tk
import threading
import time
from create_board import create_board
from create_snake import create_snake
from show_snake import show_snake_after_move
from change_direction import change_direction
from move_snake_one_step import move_snake_one_step
from delete_current_snake import delete_current_snake_tail
from create_apple import create_apple
from is_snake_won import is_snake_won
from clean_board import clean_board
from delete_all_snake import delete_all_snake


def re_game_activated():
    global re_game
    global board
    global directions
    global snake
    print("re_game_activated()")
    print(re_game)
    print(board)
    print(snake)
    re_game = True
    delete_all_snake(snake)
    board = create_board(window)
    snake = create_snake(window, board)


def change_direction_main():
    global directions
    while re_game:
        directions = change_direction(directions)
        time.sleep(0.08)
        print(directions)


def create_apple_main(board, snake):
    while re_game:
        print("\ncreate_apple thread\n")
        valid_apple_index = create_apple(board, snake)
        time.sleep(2)
        board[valid_apple_index].set_apple_on()
        time.sleep(2)


def game_cancelled_message():
    global re_game

    re_game = False
    game_cancelled_label = tk.Label(window, text="you lost")
    game_cancelled_label.grid(row=0)
    game_cancelled_label.place(x=320, y=250, anchor="center")

    #print()
    game_cancelled_button = tk.Button(window, text="play again", command=re_game_activated)
    #print(re_game)
    game_cancelled_button.grid(row=1)
    game_cancelled_button.place(x=320, y=280, anchor="center")


def snake_won():
    global re_game
    for object in window.winfo_children():
        object.destroy()

    game_cancelled_label = tk.Label(window, text="you won")
    game_cancelled_label.grid(row=0)
    game_cancelled_label.place(x=100, y=50, anchor="center")

    game_cancelled_button = tk.Button(window, text="play again", command=re_game_activated)
    game_cancelled_button.grid(row=2)
    game_cancelled_button.place(x=100, y=80, anchor="center")


def snake_moving():
    global board
    global directions
    global snake
    global keep_moving

    if keep_moving:
        try:
            delete_current_snake_tail(window, board, snake)
            #print("1")
            snake = move_snake_one_step(window, board, snake, directions["current direction"])
            print(f"len snake is: {len(snake)}")

            if len(snake) == 0:
                keep_moving = False
                clean_board(window, board)
                game_cancelled_message()
                print("entered")
                #show_snake_after_move(window, board, {})
            else:
                show_snake_after_move(window, board, snake)
            print("3")

            if is_snake_won(snake):
                snake_won()
            #print("4")

            window.after(snake_step_speed, snake_moving)
        except IndexError as e:
            print(e)
            keep_moving = False


snake_step_speed = 90
keep_moving = True
directions = {"current direction": "d", "last direction": "d"}  # = {"current direction": "d", "last direction": "d"}  # initialization only
window = tk.Tk()
board = {}  # create_board(window)  # board is a dict. keys are the index of the square and the value are the square objects
snake = {}  # create_snake(window, board)
re_game = True


board = create_board(window)  # board is a dict. keys are the index of the square and the value are the cordinates
snake = create_snake(window, board)
t1 = threading.Thread(target=change_direction_main, daemon=True)
t2 = threading.Thread(target=create_apple_main, args=(board, snake), daemon=True)
#t3 = threading.Thread(target=play_music, daemon=True)
t1.start()
t2.start()

while True:
    print(re_game)
    if re_game:
        print("if was again!")
        while re_game:
            clean_board(window, board)
            keep_moving = True
            while keep_moving:
                print("another game")
                window.after(snake_step_speed, snake_moving)
                window.mainloop()

