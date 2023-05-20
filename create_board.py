import tkinter as tk
import playsound
import threading
#from PIL import ImageTk, Image


WIDTH_CELL = 20
LENGTH_CELL = 10
snake_speed = 120
#apple_photo = tk.PhotoImage(file="apple_photo_snake_game.PNG")
class Square:

    def __init__(self, window, padx, pady, bg_color, apple_photo):
        self.cell = tk.Label(window, bg=bg_color, padx=padx, pady=pady)
        self.original_color = bg_color
        self.current_color = self.original_color
        self._apple_image = "black"
        #self._apple_image = apple_photo
        self.is_image = False

    def set_cordinates(self, row, column):
        self.cordinates = [row,column]
        self.cell.grid(row=row, column=column)

    def snake_stepped(self):
        self.current_color = "red"
        self.cell.config(bg=self.current_color)

    def snake_left(self):
        self.current_color = self.original_color
        self.cell.config(bg=self.original_color)

    def set_apple_on(self):
        if self.current_color != "red":
            self.is_image = True
            #self.cell.config(image=self._apple_image)  # seting image
            self.cell.config(bg=self._apple_image)
            return True
        print("\n\n\n check apple again\n\n\n")  # checks a place for the apple again
        return False

    def set_apple_off(self):
        play_apple_eaten_sound()
        self.is_image = False
        #self.cell.config(image="")  # removing image
        self.cell.config(bg=self.current_color)


def create_board(window):
    apple_photo = tk.PhotoImage(file="apple_photo_snake_game.PNG")
    light_green = "#04FF2E"
    dark_green = "#029202"
    #apple_image = tk.PhotoImage(file="apple_image_png.png")
    list_of_colors = [light_green, dark_green]
    board_list = []  # will contain list of all the 17 rows
    board_dict = {} # just for initialization
    for i in range(17):  # each loop is on every row (17 rows)
        for j in range(15):  # each loop is on every cell in row (15 cells in every row)
            #apple_photo = tk.PhotoImage(file="apple_photo_snake_game.PNG", )
            temp_cell = Square(window, bg_color=list_of_colors[0], padx=WIDTH_CELL, pady=LENGTH_CELL, apple_photo=apple_photo)
            temp_cell.set_cordinates(row=i, column=j)
            board_list.append(temp_cell)
            list_of_colors = list(reversed(list_of_colors))  # switching the colors places so the board will be half dark half light
    for i in range(17*15):
        board_dict[i] = board_list[i]
    return board_dict  # this is actually the board


def play_apple_eaten_sound():
    threading.Thread(target=playsound.playsound, args=('apple_eating_sound_mp3.mp3',), daemon=True).start()