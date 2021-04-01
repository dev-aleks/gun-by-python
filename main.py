import pygame as pg
import numpy
from constants import *

# initial the game:
pg.init()

# set screen:
screen_width = 800
screen_height = 800
screen = pg.display.set_mode([screen_width, screen_height])
pg.display.set_caption('GUN GAME')  # name for window

# loop until the user clicks the close button:
done = False
clock = pg.time.Clock()
max_FPS = 60


def random_color():
    return numpy.random.randint(256), numpy.random.randint(256), numpy.random.randint(256)


class Cannon:
    """
    Class for description a cannon
    """
    size_height = screen_height*0.05
    size_width = screen_width*0.05
    coordinate_x = numpy.random.randint(1, screen_width - size_width)
    coordinate_y = screen_height - size_height - 1

    def __init__(self, coordinate=[coordinate_x, coordinate_y], size=[size_width, size_height], color=None):
        self.coordinate = coordinate
        self.size = size
        if color == None:
            color = random_color()
        self.color = color

    def draw(self, screen):
        """
        Function for drawing cannon
        :param screen: surface for drawing
        :return: None
        """
        pg.draw.rect(screen, self.color, (self.coordinate, self.size))

    def move(self, step_moving):
        """
        Function for change position cannon
        :param step_moving: шаг передвижения
        :return:
        """
        self.coordinate[0] += step_moving
        if self.coordinate[0] < 0:
            self.coordinate[0] = 0
        elif self.coordinate[0] + self.size_width > screen_width:
            self.coordinate[0] = screen_width - self.size_width


class Shell:
    """
    Class for description a shell
    """
    coordinate_x = Cannon.coordinate_x + Cannon.size_height//2
    coordinate_y = Cannon.coordinate_y + Cannon.size_height//2
    radius_shell = Cannon.size_height//2

    def __init__(self, radius=radius_shell, coordinate=[coordinate_x, coordinate_y], color=None):
        self.radius = radius
        self.coordinate = coordinate
        if color == None:
            color = random_color()
        self.color = color

    def draw(self, screen, speed=1):
        pg.draw.circle(screen, self.color, self.coordinate, self.radius)
        while not self.coordinate[1] == 0:
            self.coordinate[1] -= speed

    def shooting(self):
        pass


class Target:
    """
    Класс для описания мишеней
    """
    pass


my_cannon = Cannon()
my_shell = Shell()

while not done:
    # this limits the while loop to a max of XXX times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(max_FPS)
    # exit cycle:
    for event in pg.event.get():  # user did something
        if event.type == pg.QUIT:  # if user clicked close
            done = True  # change flag; exit from loop
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                pass
    # drawing...
    # set screen background:
    screen.fill(BLACK)
    my_cannon.draw(screen)
    #my_shell.draw(screen)
    # keys rules:
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] or keys[pg.K_a]:
        my_cannon.move(-5)
    elif keys[pg.K_RIGHT] or keys[pg.K_d]:
        my_cannon.move(5)
    elif keys[pg.K_SPACE]:
        my_shell.draw(screen)
    # after all drawing commands update screen:
    pg.display.update()

# be IDLE friendly
pg.quit()
