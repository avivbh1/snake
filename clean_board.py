import tkinter as tk
from time import sleep
import threading
import playsound

count_of_cancelled_game = 0
is_game_cancelled = False
re_game = False


def clean_board(window, board):
    sleep(0.5)
    for index in board:
        board[index].snake_left


    #re_game = is_player_play_again(window)

    #print("cancel")
    #return re_game


def is_player_play_again(window):
    re_game = game_cancelled_button = tk.Button(window, text="play again", command=play_again)
    game_cancelled_button.grid(row=1)
    game_cancelled_button.place(x=320, y=280, anchor="center")
    return re_game


def play_again():
    return True


def play_failed_sound():
    threading.Thread(target=playsound.playsound, args=('snake_failed_sound.mp3',), daemon=True).start()