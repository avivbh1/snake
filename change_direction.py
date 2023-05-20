import tkinter as tk
import keyboard
import playsound
import threading


def play_change_direction_sound():
    threading.Thread(target=playsound.playsound, args=("changing_direction_sound.mp3",), daemon=True).start()


def change_direction(directions):
    current_direction = directions["current direction"]
    last_direction = directions["last direction"]
    current_key = keyboard.read_key()
    if current_key == "d" and current_direction != "a":

        last_direction = current_direction
        current_direction = "d"
        print(current_direction)
        return {"last direction": last_direction, "current direction": current_direction}

    elif current_key == "a" and current_direction != "d":

        last_direction = current_direction
        current_direction = "a"
        print(current_direction)
        return {"last direction": last_direction, "current direction": current_direction}

    elif current_key == "w" and current_direction != "s":

        last_direction = current_direction
        current_direction = "w"
        print(current_direction)
        return {"last direction": last_direction, "current direction": current_direction}

    elif current_key == "s" and current_direction != "w":

        last_direction = current_direction
        current_direction = "s"
        print(current_direction)
        return {"last direction": last_direction, "current direction": current_direction}
    else:
        return directions

#threading.Thread(target=change_direction, args=({"current direction": "w", "last direction": "d"}))
#print({"current direction": "w", "last direction": "d"})