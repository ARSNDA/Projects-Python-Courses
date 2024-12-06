import pygame
from constants import *
from random import randint


class Alien:

    def __init__(self):
        self.image = pygame.image.load('images/alien.png')
        self.width, self.height = self.image.get_size()
        self.x, self.y = randint(0, SCREEN_WIDTH - self.width), 0
        self.STEP = ALIEN_STEP
        self.speed = self.STEP

    def update_position(self):
        self.y += self.speed  # Двигаем инопланетянина только по оси Y

    def increase_speed(self):
        self.speed += self.STEP / 5

    def reset(self):
        self.x, self.y = randint(0, SCREEN_WIDTH - self.width), 0  # Сбрасываем позицию инопланетянина

    def has_reached_fighter(self, fighter):
        # Проверка, столкнулся ли инопланетянин с боевым кораблем
        return self.y + self.height >= fighter.y
