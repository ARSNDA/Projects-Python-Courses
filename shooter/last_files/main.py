import pygame  # Импортируем модуль pygame
import sys  # Импортируем модуль sys для выхода из игры
from random import randint  # Импортируем функцию randint для случайного расположения пришельцев

# Определение ширины и высоты экрана
screen_width, screen_height = 800, 600

pygame.init()  # Инициализируем все модули pygame

game_fond = pygame.font.Font(None, 30)  # Создаем объект шрифта с размером 30

# Установка режима отображения
screen = pygame.display.set_mode((screen_width, screen_height))

# Цвет фона экрана
screen_fill_color = (32, 52, 71)

# Установка заголовка окна
pygame.display.set_caption("Awesome Shooter Game")

# Загрузка и изменение размеров изображения корабля
fighter_image = pygame.image.load('../images/fighter.png')  # Загружаем изображение корабля
fighter_image = pygame.transform.scale(fighter_image, (80, 80))  # Изменяем размер изображения корабля
fighter_width, fighter_height = fighter_image.get_size()  # Получаем размеры изображения
fighter_x, fighter_y = screen_width / 2 - fighter_width / 2, screen_height - fighter_height  # Начальная позиция корабля
FIGHTER_STEP = 1  # Шаг перемещения корабля
fighter_is_mouving_left, fighter_is_mouving_right = False, False  # Флаги для отслеживания перемещения

# Загрузка и изменение размеров изображения ракеты
rocket_image = pygame.image.load('../images/rocket.png')  # Загружаем изображение ракеты
rocket_image = pygame.transform.scale(rocket_image, (40, 40))  # Изменяем размер изображения ракеты
rocket_width, rocket_height = rocket_image.get_size()  # Получаем размеры изображения ракеты
rocket_image = pygame.transform.scale(rocket_image,
                                      (rocket_width // 2, rocket_height // 2))  # Уменьшаем изображение ракеты вдвое
rocket_x, rocket_y = fighter_x + fighter_width / 2 - rocket_width / 2, fighter_y - rocket_height  # Начальная позиция ракеты
rocket_was_fired = False  # Флаг, указывающий, была ли ракета выпущена
ROCKET_STEP = 3  # Шаг перемещения ракеты

# Загрузка и изменение размеров изображения пришельца
alien_image = pygame.image.load('../images/alien.png')  # Загружаем изображение пришельца
alien_image = pygame.transform.scale(alien_image, (80, 80))  # Изменяем размер изображения пришельца
alien_width, alien_height = alien_image.get_size()  # Получаем размеры изображения пришельца
alien_image = pygame.transform.scale(alien_image,
                                     (alien_width // 2, alien_height // 2))  # Уменьшаем изображение пришельца вдвое
alien_x, alien_y = randint(0, screen_width - alien_width), 0  # Начальная позиция пришельца
ALIEN_STEP = 0.2  # Шаг перемещения пришельца
alien_speed = ALIEN_STEP  # Скорость перемещения пришельца

# Загрузка и изменение размеров фонового изображения
fon_image = pygame.image.load('../images/fon.png')  # Загружаем фоновое изображение
fon_image = pygame.transform.scale(fon_image, (
screen_width, screen_height))  # Изменяем размер фонового изображения до размера экрана
fon_width, fon_height = fon_image.get_size()  # Получаем размеры фонового изображения

# Основной цикл игры
game_is_running = True
game_score = 0  # Счет игры
while game_is_running:
    for event in pygame.event.get():  # Обрабатываем все события
        if event.type == pygame.QUIT:  # Проверяем, если событие закрытия окна
            sys.exit()  # Выходим из игры
        if event.type == pygame.KEYDOWN:  # Проверяем, если клавиша нажата
            if event.key == pygame.K_LEFT:  # Нажата стрелка влево
                fighter_is_mouving_left = True  # Устанавливаем флаг перемещения влево
            if event.key == pygame.K_RIGHT:  # Нажата стрелка вправо
                fighter_is_mouving_right = True  # Устанавливаем флаг перемещения вправо
            if event.key == pygame.K_SPACE:  # Нажата пробел
                rocket_was_fired = True  # Устанавливаем флаг, что ракета выпущена
                rocket_x = fighter_x + fighter_width / 2 - rocket_width / 2  # Начальная позиция ракеты по X
                rocket_y = fighter_y - rocket_height  # Начальная позиция ракеты по Y
        if event.type == pygame.KEYUP:  # Проверяем, если клавиша отпущена
            if event.key == pygame.K_LEFT:  # Стрелка влево отпущена
                fighter_is_mouving_left = False  # Сбрасываем флаг перемещения влево
            if event.key == pygame.K_RIGHT:  # Стрелка вправо отпущена
                fighter_is_mouving_right = False  # Сбрасываем флаг перемещения вправо

    if fighter_is_mouving_left and fighter_x >= FIGHTER_STEP:  # Проверяем, если флаг перемещения влево установлен и корабль находится в пределах экрана
        fighter_x -= FIGHTER_STEP  # Перемещаем корабль влево на один шаг

    if fighter_is_mouving_right and fighter_x <= screen_width - fighter_width - FIGHTER_STEP:  # Проверяем, если флаг перемещения вправо установлен и корабль находится в пределах экрана
        fighter_x += FIGHTER_STEP  # Перемещаем корабль вправо на один шаг

    alien_y += alien_speed  # Перемещаем пришельца вниз на один шаг

    if rocket_was_fired and rocket_y + rocket_height < 0:  # Проверяем, если ракета вышла за экран
        rocket_was_fired = False  # Сбрасываем флаг, что ракета выпущена

    if rocket_was_fired:  # Проверяем, если ракета была выпущена
        rocket_y -= ROCKET_STEP  # Перемещаем ракету вверх на один шаг

    screen.fill(screen_fill_color)  # Заполняем экран цветом фона
    screen.blit(fighter_image, (fighter_x, fighter_y))  # Отображаем изображение корабля на текущей позиции
    screen.blit(alien_image, (alien_x, alien_y))  # Отображаем изображение пришельца на текущей позиции

    if rocket_was_fired:  # Проверяем, если ракета была выпущена
        screen.blit(rocket_image, (rocket_x, rocket_y))  # Отображаем изображение ракеты на текущей позиции

    # Отображаем счет игры на экране
    game_score_text = game_fond.render(f"Your Score is: {game_score}", True, (255, 255, 255))
    screen.blit(game_score_text, (20, 20))  # Отображаем текст счета на экране

    pygame.display.update()  # Обновляем экран для отображения изменений

    # Проверяем столкновение ракеты с пришельцем
    if (rocket_was_fired and \
            alien_x < rocket_x < alien_x + alien_width - rocket_width and \
            alien_y < rocket_y < alien_y + alien_height - rocket_height):
        rocket_was_fired = False  # Сбрасываем флаг, что ракета выпущена
        alien_x, alien_y = randint(0, screen_width - alien_width), 0  # Перемещаем пришельца на новую позицию
        alien_speed += ALIEN_STEP / 5  # Увеличиваем скорость пришельца
        game_score += 1  # Увеличиваем счет игры

    # Проверяем, если пришелец достиг позиции корабля
    if alien_y + alien_height > fighter_y:
        game_is_running = False  # Останавливаем игру

# Отображаем текст "GAME OVER" по центру экрана
game_over_text = game_fond.render("GAME OVER", True, (255, 255, 255))  # Создаем текст "GAME OVER"
game_over_rectangle = game_over_text.get_rect()  # Получаем прямоугольник текста
game_over_rectangle.center = (screen_width // 2, screen_height // 2)  # Устанавливаем позицию по центру экрана
screen.blit(game_over_text, game_over_rectangle)  # Отображаем текст на экране
pygame.display.update()  # Обновляем экран для отображения текста
pygame.time.wait(5000)  # Ждем 5 секунд

pygame.quit()  # Завершаем работу pygame
