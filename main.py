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
    circle = Circle(100, 100, -1, 1, 20, [255, 0, 0])

    timer = pg.time.Clock()  # Таймер, будет следить за временем
    running = True
    while running:
        timer.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # Тут будет обновление и отрисовка

        circle.x += circle.speed_x
        circle.y += circle.speed_y

        top, bottom = circle.y - circle.radius, circle.y + circle.radius
        left, right = circle.x - circle.radius, circle.x + circle.radius

        if right >= screen.get_width() or left <= 0:
            circle.speed_x *= -1
        if bottom >= screen.get_height() or top <= 0:
            circle.speed_y *= -1

        screen.fill((0, 0, 0))
        pg.draw.circle(screen, circle.color, (circle.x, circle.y), circle.radius)
        pg.display.update()


if __name__ == '__main__':
    main()