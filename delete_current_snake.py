
def delete_current_snake_tail(window, board, snake):
    """
    we need to delete the current snake on the board
    which means to return all of his squres to their original color
    also we delete the tail square of the snake
    :param window:
    :param board:
    :param snake:
    :return:
    """
    snake_tail_index = list(snake.keys())[0]
    for index in board:  # board contains index and square object
        if index == snake_tail_index:
            board[index].snake_left()
    #print("aviv" + str(snake))