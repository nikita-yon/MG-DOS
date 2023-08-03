import os
import msvcrt
import random
import time

# Определение размеров экрана консоли
CONSOLE_WIDTH = 50
CONSOLE_HEIGHT = 20

# Начальные координаты мяча и платформы
ball_x, ball_y = CONSOLE_WIDTH // 2, CONSOLE_HEIGHT // 2
platform_x = CONSOLE_WIDTH // 2 - 5

# Начальные параметры движения мяча
ball_speed_x = 1
ball_speed_y = -1

# Число жизней
lives = 5

frames = 0
start_time = time.perf_counter()

# Функция отрисовки игрового экрана
def draw_game():
    os.system("cls")
    for y in range(CONSOLE_HEIGHT):
        for x in range(CONSOLE_WIDTH):
            if (x == ball_x and y == ball_y) or (x in range(platform_x, platform_x + 10) and y == CONSOLE_HEIGHT - 1):
                print("O", end="")
            elif y == 0 or y == CONSOLE_HEIGHT - 1 or x == 0 or x == CONSOLE_WIDTH - 1:
                print("#", end="")
            else:
                print(" ", end="")
        print()
    print("Lives:", lives)
    print("Ball: x-{} y-{}".format(ball_x, ball_y))
    print("Platform: x-{}".format(platform_x))
    print("FPS: {:.2f}".format(frames / (time.perf_counter() - start_time)))  # Отображаем FPS с двумя знаками после запятой


# Основной цикл игры
while lives > 0:
    # Отрисовка игрового экрана
    draw_game()

    # Обработка управления платформой
    if msvcrt.kbhit():
        key = msvcrt.getch().decode("utf-8").lower()
        if key == "a" and platform_x > 1:
            platform_x -= 3  # Увеличиваем скорость движения платформы
        elif key == "d" and platform_x < CONSOLE_WIDTH - 11:
            platform_x += 3  # Увеличиваем скорость движения платформы

    # Обновление координат мяча
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Отскок мяча от стен
    if ball_x == 1 or ball_x == CONSOLE_WIDTH - 2:
        ball_speed_x = -ball_speed_x
    if ball_y == 1:
        ball_speed_y = -ball_speed_y

    # Отскок мяча от платформы
    if ball_y == CONSOLE_HEIGHT - 2 and platform_x <= ball_x < platform_x + 10:
        ball_speed_y = -ball_speed_y

    # Проверка на поражение (мяч упал)
    if ball_y == CONSOLE_HEIGHT - 1:
        lives -= 1
        ball_x, ball_y = CONSOLE_WIDTH // 2, CONSOLE_HEIGHT // 2
        ball_speed_x = random.choice([-1, 1])
        ball_speed_y = -1

    # Задержка для более плавного движения
    time.sleep(0.02)  # Уменьшаем задержку для более быстрого движения

# По достижении этой точки, у вас закончились жизни, и игра завершается.
print("Вы проиграли!")
