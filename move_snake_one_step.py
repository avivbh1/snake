import tkinter as tk
import keyboard
#from game_cancelled import game_cancelled
from collections import OrderedDict
import threading
import playsound

def adding_node_after_eating(board, snake, snake_tail_key ,snake_before_tail_key):
    temp_dict_as_snake = snake

    if snake_before_tail_key - snake_tail_key == 1:
        new_snake = {snake_tail_key - 1: board[snake_tail_key - 1]}

    elif snake_before_tail_key - snake_tail_key == -1:
        new_snake = {snake_tail_key + 1: board[snake_tail_key + 1]}

    elif snake_before_tail_key - snake_tail_key == 15:
        new_snake = {snake_tail_key - 15: board[snake_tail_key - 15]}

    elif snake_before_tail_key - snake_tail_key == -15:
        new_snake = {snake_tail_key + 15: board[snake_tail_key + 15]}

    new_snake.update(snake)
    return new_snake


def move_snake_one_step(window, board, snake, current_direction):
    snake_clone = snake  # thats for an error to occured so we could return the original snake so the main will realize there was an error
    """
    build new head for the snake
    :param window:
    :param board:
    :param snake:
    :param current_direction:
    :return:
    """
    try:
        print(snake, "ddsdsdsdsd")
        temp_snake_keys = list(snake.keys())  # creating list of all the indexs
        snake_head_key = temp_snake_keys[-1]
        snake_before_head_key = temp_snake_keys[-2]
        snake_tail_key = temp_snake_keys[0]  # tail of the snake key
        snake_before_tail_key = temp_snake_keys[1]
        del snake[snake_tail_key]

        if not board[snake_head_key].is_image:  # image is apple
            temp_snake_keys = temp_snake_keys[1:]  # slicing the tail key
            print("is image -  " + str(snake))

        if board[snake_head_key].is_image: # image is apple

            snake = adding_node_after_eating(board, snake, snake_tail_key, snake_before_tail_key)

            board[snake_head_key].set_apple_off()

        if current_direction == "w":
            try:
                if snake_head_key < 15:
                    # checks if the snake touching the upside border
                    raise KeyError
                elif board[snake_head_key - 15].current_color == "red":
                    #  checks if the snake touches himself
                    print("snake touched himself")
                    raise KeyError
                else:
                    snake[snake_head_key-15] = board[snake_head_key - 15]
            except KeyError as snake_failed_Error:
                #play_failed_sound()
                #game_cancelled(window, snake)  # to return false
                return {}  # it means snake didnt move so the main will understand there was an error

        elif current_direction == "d":
            try:
                if (snake_head_key + 1) % 15 == 0:
                    #  checks if the snake touches the right border
                    print("touches the right border")
                    raise KeyError
                elif board[snake_head_key + 1].current_color == "red":
                    # checks if the snake touches himself
                    print("snake touched himself")
                    raise KeyError
                else:
                    snake[snake_head_key + 1] = board[snake_head_key + 1]
            except KeyError:
                #play_failed_sound()
                #game_cancelled(window, snake)
                return {}  # it means snake didnt move so the main will understand there was an error

        elif current_direction == "s":
            try:
                if snake_head_key > 240:
                    #  checks if the snake touches the upside border
                    raise KeyError
                if board[snake_head_key + 15].current_color == "red":
                    #  checks if the snakes touch himself
                    raise KeyError

                else:
                    snake[snake_head_key + 15] = board[snake_head_key + 15]
            except KeyError:
                #play_failed_sound()
                #game_cancelled(window, snake)
                return {}  # it means snake didnt move so the main will understand there was an error


        elif current_direction == "a":
            try:
                if snake_head_key % 15 == 0:
                    print("snake touched the left border")
                    raise KeyError
                elif board[snake_head_key - 1].current_color == "red":
                    #  cheks if the snake touched himself
                    print("snake touched himself")
                    raise KeyError
                else:
                    snake[snake_head_key - 1] = board[snake_head_key - 1]
            except KeyError:
                #play_failed_sound()
                #game_cancelled(window, snake)
                return {}  # empty snake



        return snake
    except KeyError:
        #play_failed_sound()
        #game_cancelled(window, snake)
        return {}  # empty snake
"""        for object in window.winfo_children():
            object.destroy()
        game_canceled_label = tk.Label(text="you lose!")
            #game_canceled_label.pack()
        game_canceled_label.grid()"""


