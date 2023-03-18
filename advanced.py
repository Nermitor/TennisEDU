from dataclasses import dataclass
from random import choice

import pygame as pg


@dataclass
class Circle:
    x: int
    y: int
    speed_x: int
    speed_y: int
    radius: int
    color: list


@dataclass
class Rocket:
    x: int
    y: int
    speed_y: int
    height: int
    width: int
    color: list


def new_ball(screen: pg.Surface):
    speed_x, speed_y = 5 * choice([-1, 1]), 5 * choice([-1, 1])
    return Circle(screen.get_width() // 2, screen.get_height() // 2, speed_x, speed_y, 20, [255, 0, 0])


def draw_score(screen: pg.Surface, score):
    font = pg.font.SysFont("Arial", 20)
    screen.blit(font.render(f"{score[0]} - {score[1]}", True, [255] * 3), (screen.get_width() / 2, 50))


def main():
    screen_size = [800, 500]
    fps = 60

    pg.init()  # Инициализация модуля
    screen = pg.display.set_mode(screen_size)  # Настройка экрана

    # Круг с центром в точке (100; 100), скоростью по x = -10, y = 10, радиусом 20, и красным цветом.
    ball = new_ball(screen)

    first_player_score, second_player_score = 0, 0
    first_rocket = Rocket(20, 100, 10, 100, 20, [255] * 3)
    second_rocket = Rocket(screen.get_width() - 20, 100, 10, 100, 20, [255] * 3)

    timer = pg.time.Clock()  # Таймер, будет следить за временем
    running = True
    while running:
        timer.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # Смотрим, какие клавиши зажаты и двигаем в зависимости от них ракетки
        if pg.key.get_pressed()[pg.K_w]:
            first_rocket.y -= first_rocket.speed_y
        if pg.key.get_pressed()[pg.K_s]:
            first_rocket.y += first_rocket.speed_y
        if pg.key.get_pressed()[pg.K_UP]:
            second_rocket.y -= first_rocket.speed_y
        if pg.key.get_pressed()[pg.K_DOWN]:
            second_rocket.y += first_rocket.speed_y

        # Ограничение ракеток по высоте
        second_rocket.y = max(0, min(second_rocket.y, screen.get_height() - second_rocket.height))
        first_rocket.y = max(0, min(first_rocket.y, screen.get_height() - first_rocket.height))

        # Движение шарика
        ball.x += ball.speed_x
        ball.y += ball.speed_y

        # Самая верхняя, нижняя, левая, правая точка шарика
        top, bottom = ball.y - ball.radius, ball.y + ball.radius
        left, right = ball.x - ball.radius, ball.x + ball.radius

        # Если шарик был пропущен (вышел за левую или правою границу
        if right >= screen.get_width():
            first_player_score += 1  # Добавляем первому игроку очко
            ball = new_ball(screen)  # Обновляем мяч, чтобы он появился в середине
        if left <= 0:
            second_player_score += 1
            ball = new_ball(screen)

        if bottom >= screen.get_height():  # Если шарик пересекает нижнюю границу
            ball.speed_y = -abs(ball.speed_y)  # Изменяем скорость, чтобы её вектор был направлен вверх
        elif top <= 0:
            ball.speed_y = abs(ball.speed_y)

        if left <= first_rocket.x + first_rocket.width:
            # Проверка на пересечение с ракеткой
            if ball.y in range(first_rocket.y - 10, first_rocket.y + first_rocket.height + 1 + 10):
                ball.speed_x = abs(ball.speed_x)
        if right >= second_rocket.x:
            if ball.y in range(second_rocket.y - 10, second_rocket.y + second_rocket.height + 1 + 10):
                ball.speed_x = -abs(ball.speed_x)

        screen.fill((0, 0, 0))
        pg.draw.circle(screen, ball.color, (ball.x, ball.y), ball.radius)
        pg.draw.rect(screen, first_rocket.color,
                     [first_rocket.x, first_rocket.y, first_rocket.width, first_rocket.height])
        pg.draw.rect(screen, second_rocket.color,
                     [second_rocket.x, second_rocket.y, second_rocket.width, second_rocket.height])
        draw_score(screen, (first_player_score, second_player_score))
        pg.display.update()


if __name__ == '__main__':
    main()
