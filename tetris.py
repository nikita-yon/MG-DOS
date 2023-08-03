import random
import time
import os
import keyboard

width = int(input("width>"))
height = int(input("height>"))
WIDTH = width
HEIGHT = height
EMPTY = ' '
BLOCK = 'X'

SHAPES = [
    [[BLOCK, BLOCK],
     [BLOCK, BLOCK]],
    [[BLOCK, BLOCK, BLOCK],
     [EMPTY, BLOCK, EMPTY]],
    [[BLOCK, BLOCK, BLOCK],
     [EMPTY, EMPTY, BLOCK]],
    [[BLOCK, BLOCK, BLOCK],
     [BLOCK, EMPTY, EMPTY]],
    [[BLOCK, BLOCK, EMPTY],
     [EMPTY, BLOCK, BLOCK]],
    [[EMPTY, BLOCK, BLOCK],
     [BLOCK, BLOCK, EMPTY]],
]

def create_board():
    return [[EMPTY for _ in range(WIDTH)] for _ in range(HEIGHT)]

def draw_board(board, shape, x, y, score):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in range(HEIGHT):
        for col in range(WIDTH):
            if row >= y and row < y + len(shape) and col >= x and col < x + len(shape[0]):
                if shape[row - y][col - x] == BLOCK:
                    print(BLOCK, end='')
                else:
                    print(board[row][col], end='')
            else:
                print(board[row][col], end='')
        print()
    print("Score:", score)

def check_collision(board, shape, x, y):
    for row in range(len(shape)):
        for col in range(len(shape[0])):
            if shape[row][col] == BLOCK:
                if y + row >= HEIGHT or x + col < 0 or x + col >= WIDTH or board[y + row][x + col] == BLOCK:
                    return True
    return False

def add_shape_to_board(board, shape, x, y):
    for row in range(len(shape)):
        for col in range(len(shape[0])):
            if shape[row][col] == BLOCK:
                board[y + row][x + col] = BLOCK

def rotate_shape(shape):
    return [list(reversed(row)) for row in zip(*shape)]

def remove_completed_rows(board):
    completed_rows = []
    for row in range(HEIGHT):
        if all(cell == BLOCK for cell in board[row]):
            completed_rows.append(row)

    for row in completed_rows:
        del board[row]
        board.insert(0, [EMPTY for _ in range(WIDTH)])

def get_input():
    if keyboard.is_pressed('a'):
        return 'left'
    elif keyboard.is_pressed('d'):
        return 'right'
    elif keyboard.is_pressed('s'):
        return 'down'
    elif keyboard.is_pressed('w'):
        return 'rotate'
    elif keyboard.is_pressed('q'):
        return 'quit'
    return None

def get_drop_position(board, shape, x, y):
    while not check_collision(board, shape, x, y + 1):
        y += 1
    return y

def main():
    board = create_board()
    current_shape = random.choice(SHAPES)
    x, y = WIDTH // 2 - len(current_shape[0]) // 2, 0
    score = 0
    drop_time = time.time()

    while True:
        preview_board = [row[:] for row in board]
        drop_position = get_drop_position(preview_board, current_shape, x, y)

        action = get_input()

        if action == 'quit':
            break
        if action == 'left':
            if not check_collision(board, current_shape, x - 1, y):
                x -= 1
        elif action == 'right':
            if not check_collision(board, current_shape, x + 1, y):
                x += 1
        elif action == 'down':
            if not check_collision(board, current_shape, x, y + 1):
                y += 1
        elif action == 'rotate':
            rotated_shape = rotate_shape(current_shape)
            if not check_collision(board, rotated_shape, x, y):
                current_shape = rotated_shape

        if time.time() - drop_time > 0.5:  # Устанавливаем задержку падения фигуры в 0.5 секунды
            drop_time = time.time()
            if y < drop_position:
                y += 1

        if check_collision(board, current_shape, x, y + 1):
            add_shape_to_board(board, current_shape, x, y)
            remove_completed_rows(board)
            current_shape = random.choice(SHAPES)
            x, y = WIDTH // 2 - len(current_shape[0]) // 2, 0
            drop_position = get_drop_position(board, current_shape, x, y)
            if check_collision(board, current_shape, x, y):
                break
            score += 1

        draw_board(preview_board, current_shape, x, y, score)
        time.sleep(0.1)

    draw_board(board, current_shape, x, y, score)
    os.system("cls")
    print("Game Over. Your score:", score)

if __name__ == "__main__":
    main()
