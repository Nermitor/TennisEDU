from dataclasses import dataclass

import pygame as pg
from pygame.color import THECOLORS


@dataclass
class Circle:
    x: int
    y: int
    speed_x: int
    speed_y: int
    radius: int
    color: tuple[int, int, int, int]


def main():
    pg.init()
    screen_size = (800, 500)
    screen = pg.display.set_mode(screen_size)

    speed_x, speed_y = 10, 10
    diameter = 50
    fps = 60

    circle = Circle(100, 100, -10, 10, 20, THECOLORS['red'])

    timer = pg.time.Clock()

    running = True
    while running:
        timer.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        circle.x += circle.speed_x
        circle.y += circle.speed_y

        if circle.x + circle.radius >= screen.get_width() or circle.x - circle.radius <= 0:
            circle.speed_x *= -1
        if circle.y + circle.radius >= screen.get_height() or circle.y - circle.radius <= 0:
            circle.speed_y *= -1

        pg.draw.circle(screen, circle.color, (circle.x, circle.y), circle.radius)

        pg.display.flip()
        screen.fill((0, 0, 0))


if __name__ == '__main__':
    main()
