import pygame
from constants import *


class Rocket:

    def __init__(self, fighter):
        self.image = pygame.image.load('images/rocket.png')
        self.width, self.height = self.image.get_size()
        self.x, self.y = SCREEN_WIDTH - self.width, SCREEN_HEIGHT - self.height
        self.STEP = ROCKET_STEP
        self.was_fired = False
        self.fighter = fighter

    def fire(self):
        self.was_fired = True
        self.x = self.fighter.x + self.fighter.width / 2 - self.width / 2
        self.y = self.fighter.y - self.height

    def update_position(self):
        if self.was_fired:
            self.y -= self.STEP

    def is_out_of_screen(self):
        return self.y + self.height < 0

    def reset(self):
        self.was_fired = False

    def is_collision(self, alien):
        collision_detected = self.x < alien.x + alien.width and \
                             self.x + self.width > alien.x and \
                             self.y < alien.y + alien.height and \
                             self.y + self.height > alien.y
        if collision_detected:
            alien.update_position()  # Возрождаем инопланетянина в новой позиции
        return collision_detected
