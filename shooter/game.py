import pygame
import sys
from fighter import Fighter
from alien import Alien
from rocket import Rocket
from constants import *


class Game:
    def __init__(self):
        pygame.display.set_caption(GAME_CAPTION)  # Устанавливаем заголовок окна
        self.screen_width, self.screen_height = SCREEN_WIDTH, SCREEN_HEIGHT  # Задаем ширину и высоту экрана
        self.screen_fill_color = SCREEN_FILL_COLOR  # Цвет заливки экрана
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))  # Создаем окно игры с заданными размерами
        self.game_font = pygame.font.Font(None, 30)  # Задаем шрифт для текста игры
        self.game_score = 0  # Инициализируем счет игры
        self.fighter = Fighter()  # Создаем объект класса Fighter (боевой корабль)
        self.alien = Alien()  # Создаем объект класса Alien (инопланетянин)
        self.rocket = Rocket(self.fighter)  # Создаем объект класса Rocket (ракета)
        self.game_is_running = True  # Флаг, указывающий на то, что игра продолжается

    def run(self):
        while self.game_is_running:  # Основной игровой цикл
            for event in pygame.event.get():  # Перебираем все события в очереди событий
                if event.type == pygame.QUIT:  # Проверяем, было ли событие выхода из игры
                    sys.exit()  # Завершаем выполнение программы
                self.handle_key_events(event)  # Обрабатываем события клавиатуры
            self.update_game_state()  # Обновляем состояние игры
            self.draw_screen()  # Отрисовываем экран
        self.show_game_over()  # Показать экран с сообщением о завершении игры

    def handle_key_events(self, event):
        if event.type == pygame.KEYDOWN:  # Проверяем, была ли нажата клавиша
            if event.key == pygame.K_LEFT:  # Если была нажата клавиша влево
                self.fighter.move_left()  # Двигаем боевой корабль влево
            if event.key == pygame.K_RIGHT:  # Если была нажата клавиша вправо
                self.fighter.move_right()  # Двигаем боевой корабль вправо
            if event.key == pygame.K_SPACE:  # Если была нажата клавиша пробела
                self.rocket.fire()  # Запускаем ракету
        if event.type == pygame.KEYUP:  # Проверяем, была ли отпущена клавиша
            if event.key == pygame.K_LEFT:  # Если была отпущена клавиша влево
                self.fighter.stop_moving()  # Останавливаем движение боевого корабля влево
            if event.key == pygame.K_RIGHT:  # Если была отпущена клавиша вправо
                self.fighter.stop_moving()  # Останавливаем движение боевого корабля вправо

    def update_game_state(self):
        self.fighter.update_position()  # Обновляем позицию боевого корабля
        self.alien.update_position()  # Обновляем позицию инопланетянина
        self.rocket.update_position()  # Обновляем позицию ракеты

        if self.rocket.is_out_of_screen():  # Проверяем, вышла ли ракета за экран
            self.rocket.reset()  # Возвращаем ракету в исходное положение

        if self.rocket.is_collision(self.alien):  # Проверяем, столкнулась ли ракета с инопланетянином
            self.rocket.reset()  # Возвращаем ракету в исходное положение
            self.game_score += 1  # Увеличиваем счет игры на 1
            self.alien.reset()  # Сбрасываем инопланетянина в исходное положение

        if self.alien.has_reached_fighter(self.fighter):  # Проверяем, достиг ли инопланетянин боевого корабля
            self.game_is_running = False  # Завершаем игру

    def draw_screen(self):
        self.screen.fill(self.screen_fill_color)  # Заливаем экран цветом
        self.screen.blit(self.fighter.image, (self.fighter.x, self.fighter.y))  # Отрисовываем боевой корабль
        self.screen.blit(self.alien.image, (self.alien.x, self.alien.y))  # Отрисовываем инопланетянина
        if self.rocket.was_fired:  # Проверяем, была ли выпущена ракета
            self.screen.blit(self.rocket.image, (self.rocket.x, self.rocket.y))  # Отрисовываем ракету
        self.show_game_score()  # Отображаем счет игры
        pygame.display.update()  # Обновляем экран

    def show_game_score(self):
        game_score_text = self.game_font.render(f"Your Score is: {self.game_score}", True,
                                                (255, 255, 255))  # Создаем текст с текущим счетом игры
        self.screen.blit(game_score_text, (10, 10))  # Отображаем счет игры на экране

    def show_game_over(self):
        game_over_text = self.game_font.render("GAME OVER", True,
                                               (255, 255, 255))  # Создаем текст с сообщением о завершении игры
        game_over_rectangle = game_over_text.get_rect()  # Получаем прямоугольник ограничивающий текст
        game_over_rectangle.center = (
        self.screen_width / 2, self.screen_height / 2)  # Центрируем прямоугольник по центру экрана
        self.screen.blit(game_over_text, (
        self.screen_width / 2 - 100, self.screen_height / 2 - 50))  # Отображаем сообщение о завершении игры на экране
        pygame.display.update()  # Обновляем экран
        pygame.time.wait(5000)  # Ждем 5 секунд перед завершением программы

