import os
import time
import random
import keyboard

WIDTH = 50
HEIGHT = 20
PLAYER_CHAR = '^'
ENEMY_CHAR = '.'
BULLET_CHAR = '|'
ENEMY_SPEED = 0.1
BULLET_SPEED = 0.2
ENEMY_PROBABILITY = 0.4

player_x = WIDTH // 2
player_y = HEIGHT - 1
bullet_x = player_x
bullet_y = player_y - 1
bullet_exists = False
enemies = []
screen = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]

def update_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in screen:
        print(''.join(row))

def update_player(direction):
    global player_x
    if direction == 'left' and player_x > 0:
        player_x -= 1
    elif direction == 'right' and player_x < WIDTH - 1:
        player_x += 1

def update_bullet():
    global bullet_x, bullet_y, bullet_exists
    if bullet_exists:
        bullet_y -= 1
        if bullet_y < 0:
            bullet_exists = False

def update_enemies():
    global enemies
    new_enemies = []
    for enemy_x, enemy_y in enemies:
        enemy_y += ENEMY_SPEED
        if enemy_y < HEIGHT:
            new_enemies.append((enemy_x, enemy_y))
    enemies = new_enemies

def check_collisions():
    global bullet_x, bullet_y, bullet_exists, enemies
    if bullet_exists:
        for enemy_x, enemy_y in enemies:
            if enemy_y == bullet_y and enemy_x == bullet_x:
                enemies.remove((enemy_x, enemy_y))
                bullet_exists = False
                break
    for enemy_x, enemy_y in enemies:
        if enemy_y == player_y and enemy_x == player_x:
            return True

    return False

while True:
    if keyboard.is_pressed('left'):
        update_player('left')
    elif keyboard.is_pressed('right'):
        update_player('right')
    update_bullet()
    if random.random() < ENEMY_PROBABILITY:
        enemy_x = random.randint(0, WIDTH - 1)
        enemy_y = 0
        enemies.append((enemy_x, enemy_y))
    update_enemies()
    if check_collisions():
        break

    screen = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    screen[player_y][player_x] = PLAYER_CHAR
    if bullet_exists:
        screen[bullet_y][bullet_x] = BULLET_CHAR
    for enemy_x, enemy_y in enemies:
        screen[int(enemy_y)][int(enemy_x)] = ENEMY_CHAR
    update_screen()
    time.sleep(0.01)
    if keyboard.is_pressed('Esc'):
        break