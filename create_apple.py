import random
from time import sleep


def rand_square_for_apple(snake):
    last_square_index = 255
    first_square_index = 0
    random_square_index = list(snake.keys())[0]  # just for the loop to work
    while random_square_index in list(snake.keys()):
        random_square_index = random.randint(first_square_index, last_square_index)
    return random_square_index


def there_is_apple_in_board(board):
    for i in range(255):
        if board[i].is_image:
            return True
    return False


def place_apple(board, index):
    apple_placed = False
    while there_is_apple_in_board(board):
        pass
    while not apple_placed:
        apple_placed = board[index].set_apple_on()


def create_apple(board, snake):
    while there_is_apple_in_board(board):
        sleep(0.005)
        #print("a")
        pass  # just waiting in hope for apple to be eaten
    valid_apple_index = rand_square_for_apple(snake)
    #place_apple(board, valid_apple_index)
    return valid_apple_index

