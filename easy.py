from dataclasses import dataclass

import pygame as pg


@dataclass
class Circle:
    x: int
    y: int
    speed_x: int
    speed_y: int
    radius: int
    color: list


def main():
    screen_size = [800, 500]
    fps = 60

    pg.init()  # Инициализация модуля
    screen = pg.display.set_mode(screen_size)  # Настройка экрана

    # Круг с центром в точке (100; 100), скоростью по x = -10, y = 10, радиусом 20, и красным цветом.
    ball = Circle(100, 100, -10, 10, 20, [255, 0, 0])

    timer = pg.time.Clock()  # Таймер, будет следить за временем
    running = True
    while running:
        timer.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        ball.x += ball.speed_x
        ball.y += ball.speed_y

        top, bottom = ball.y - ball.radius, ball.y + ball.radius
        left, right = ball.x - ball.radius, ball.x + ball.radius

        if right >= screen.get_width() or left <= 0:
            ball.speed_x *= -1
        if bottom >= screen.get_height() or top <= 0:
            ball.speed_y *= -1

        screen.fill((0, 0, 0))
        pg.draw.circle(screen, ball.color, (ball.x, ball.y), ball.radius)
        pg.display.update()


if __name__ == '__main__':
    main()