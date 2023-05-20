def delete_all_snake(snake):
    for index_of_square in snake:
        snake[index_of_square].snake_left()

