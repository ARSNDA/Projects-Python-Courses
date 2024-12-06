import pygame
from constants import *


class Fighter:
    def __init__(self):
        # Загружаем изображение боевого корабля
        self.image = pygame.image.load('images/fighter.png')
        # Устанавливаем коэффициент уменьшения (например, 0.5 для уменьшения до 50% оригинального размера)
        scale_factor = 0.2
        # Получаем размеры изображения и применяем коэффициент уменьшения
        original_width, original_height = self.image.get_size()
        self.width, self.height = int(original_width * scale_factor), int(original_height * scale_factor)
        # Масштабируем изображение боевого корабля
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        # Задаём начальные координаты боевого корабля
        self.x, self.y = SCREEN_WIDTH / 2 - self.width / 2, SCREEN_HEIGHT - self.height
        # Шаг перемещения боевого корабля
        self.STEP = FIGHTER_STEP
        # Флаги для определения направления движения
        self.is_moving_left, self.is_moving_right = False, False

    def move_left(self):
        # Устанавливаем флаг движения влево
        self.is_moving_left = True

    def move_right(self):
        # Устанавливаем флаг движения вправо
        self.is_moving_right = True

    def stop_moving(self):
        # Сбрасываем флаги движения
        self.is_moving_left = False
        self.is_moving_right = False

    def update_position(self):
        # Обновляем позицию боевого корабля в зависимости от флагов движения
        if self.is_moving_left and self.x >= FIGHTER_STEP:
            # Если корабль двигается влево и находится в пределах экрана, перемещаем его влево
            self.x -= FIGHTER_STEP
        if self.is_moving_right and self.x <= SCREEN_WIDTH - self.width - self.STEP:
            # Если корабль двигается вправо и находится в пределах экрана, перемещаем его вправо
            self.x += self.STEP
