import pygame
import random
import sys
import time

# Определение ширины и высоты экрана
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

# Инициализация Pygame
pygame.init()

# Установка режима отображения
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Установка заголовка окна
pygame.display.set_caption("Awesome Shooter Game")

# Попытка загрузить изображения, если возникнет ошибка, завершить программу
try:
    BACKGROUND_IMAGE = pygame.image.load('../images/fon.png')
    BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (SCREEN_WIDTH, SCREEN_HEIGHT))  # масштабирование фона
    FIGHTER_IMAGE = pygame.image.load('../images/fighter.png')
    ALIEN_IMAGE = pygame.image.load('../images/alien.png')
    ROCKET_IMAGE = pygame.image.load('../images/rocket.png')
except pygame.error as e:
    print(f"Error loading image: {e}")
    pygame.quit()
    sys.exit()

# Изменение размеров изображений
FIGHTER_IMAGE = pygame.transform.scale(FIGHTER_IMAGE, (80, 80))
ALIEN_IMAGE = pygame.transform.scale(ALIEN_IMAGE, (40, 40))
ROCKET_IMAGE = pygame.transform.scale(ROCKET_IMAGE, (20, 20))

# Получение размеров изображений
FIGHTER_WIDTH, FIGHTER_HEIGHT = FIGHTER_IMAGE.get_size()
ALIEN_WIDTH, ALIEN_HEIGHT = ALIEN_IMAGE.get_size()
ROCKET_WIDTH, ROCKET_HEIGHT = ROCKET_IMAGE.get_size()

# Параметры начальной игры
INITIAL_ALIEN_SPEED = 5
ALIEN_SPEED_INCREMENT = 0.5
LEVEL_UP_INTERVAL = 10
ROCKET_SPEED = 3  # замедлили скорость ракеты


# Функция для появления нового пришельца в случайной позиции
def spawn_alien():
    alien_x = random.randint(0, SCREEN_WIDTH - ALIEN_WIDTH)  # случайная X координата внутри экрана
    alien_y = -ALIEN_HEIGHT  # за пределами верхней границы экрана
    return alien_x, alien_y  # вернуть координаты


# Функция для проверки столкновений
def is_collision(obj1_x, obj1_y, obj1_width, obj1_height, obj2_x, obj2_y, obj2_width, obj2_height):
    # Проверка на накладывание двух прямоугольников, представляющих объекты
    return (
            obj1_x < obj2_x + obj2_width and
            obj1_x + obj1_width > obj2_x and
            obj1_y < obj2_y + obj2_height and
            obj1_y + obj2_height > obj2_y
    )


# Функция для отображения текста на экране
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)  # создание объекта текста
    text_rect = text_obj.get_rect()  # получение прямоугольника текста
    text_rect.topleft = (x, y)  # установка позиции
    surface.blit(text_obj, text_rect)  # отрисовка текста на поверхности


# Главное меню
def main_menu():
    click = False  # переменная для отслеживания кликов мыши
    while True:
        screen.blit(BACKGROUND_IMAGE, (0, 0))  # Отрисовка фона
        draw_text('Main Menu', pygame.font.SysFont(None, 80), (255, 255, 255), screen, 275,
                  100)  # отрисовка текста меню

        mx, my = pygame.mouse.get_pos()  # получение текущей позиции мыши

        button_play = pygame.Rect(325, 250, 150, 50)  # создание прямоугольника для кнопки "Играть"
        button_quit = pygame.Rect(325, 350, 150, 50)  # создание прямоугольника для кнопки "Выйти"

        # Проверка наведения и клика на кнопку "Играть"
        if button_play.collidepoint((mx, my)) and click:
            game_loop()

        # Проверка наведения и клика на кнопку "Выйти"
        if button_quit.collidepoint((mx, my)) and click:
            pygame.quit()
            sys.exit()

        pygame.draw.rect(screen, (255, 0, 0), button_play)  # отрисовка кнопки "Играть"
        draw_text('Играть', pygame.font.SysFont(None, 40), (0, 0, 0), screen, 350, 260)  # текст на кнопке "Играть"
        pygame.draw.rect(screen, (255, 0, 0), button_quit)  # отрисовка кнопки "Выйти"
        draw_text('Выйти', pygame.font.SysFont(None, 40), (0, 0, 0), screen, 350, 360)  # текст на кнопке "Выйти"

        click = False

        for event in pygame.event.get():
            # Обработка выхода из игры
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Обработка клика мыши
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True

        pygame.display.update()  # обновление дисплея


# Основной цикл игры
def game_loop():
    # Инициализация позиции и параметров игрока
    fighter_x = SCREEN_WIDTH // 2 - FIGHTER_WIDTH // 2
    fighter_y = SCREEN_HEIGHT - FIGHTER_HEIGHT
    rockets = []
    alien_list = [spawn_alien()]

    alien_speed = INITIAL_ALIEN_SPEED
    start_time = time.time()
    last_alien_spawn_time = time.time()
    health = 3
    alien_kills = 0

    running = True
    while running:
        for event in pygame.event.get():
            # Обработка выхода из игры
            if event.type == pygame.QUIT:
                running = False
            # Обработка выстрела по клику мыши
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                rocket_x = fighter_x + FIGHTER_WIDTH // 2 - ROCKET_WIDTH // 2
                rocket_y = fighter_y - ROCKET_HEIGHT  # чтобы ракета появлялась чуть выше центра бойца
                rockets.append([rocket_x, rocket_y])

        # Обновление позиции игрока по курсору мыши
        mx, my = pygame.mouse.get_pos()
        fighter_x = mx - FIGHTER_WIDTH // 2
        fighter_x = max(0, min(SCREEN_WIDTH - FIGHTER_WIDTH, fighter_x))  # ограничение движений в пределах экрана

        # Движение пришельцев
        for i, (alien_x, alien_y) in enumerate(alien_list):
            alien_list[i] = (alien_x, alien_y + alien_speed * (1 / 60))

            # Проверка на попадание пришельца на землю
            if alien_y + ALIEN_HEIGHT >= SCREEN_HEIGHT:
                health -= 1
                alien_list.pop(i)
                if health == 0:
                    game_over()

        # Увеличение скорости пришельцев
        if time.time() - start_time > LEVEL_UP_INTERVAL:
            start_time = time.time()
            alien_speed += ALIEN_SPEED_INCREMENT

        # Возрождение новых пришельцев
        if time.time() - last_alien_spawn_time > 1:
            alien_list.append(spawn_alien())
            last_alien_spawn_time = time.time()

        # Движение ракет
        for rocket in rockets:
            rocket[1] -= ROCKET_SPEED

        # Проверка столкновений ракеты с пришельцем
        for rocket in rockets:
            for i, (alien_x, alien_y) in enumerate(alien_list):
                if is_collision(rocket[0], rocket[1], ROCKET_WIDTH, ROCKET_HEIGHT, alien_x, alien_y, ALIEN_WIDTH,
                                ALIEN_HEIGHT):
                    rockets.remove(rocket)
                    alien_list.pop(i)
                    alien_kills += 1
                    break

        # Удаление вылетевших за экран ракет и приземлившихся пришельцев
        rockets = [rocket for rocket in rockets if rocket[1] > 0]
        alien_list = [alien for alien in alien_list if alien[1] <= SCREEN_HEIGHT]

        # Заполнение экрана фоновым изображением
        screen.blit(BACKGROUND_IMAGE, (0, 0))  # отрисовка фона

        # Отрисовка объектов
        screen.blit(FIGHTER_IMAGE, (fighter_x, fighter_y))
        for alien_x, alien_y in alien_list:
            screen.blit(ALIEN_IMAGE, (alien_x, alien_y))
        for rocket in rockets:
            screen.blit(ROCKET_IMAGE, rocket)

        # Отрисовка информации об игре
        draw_text(f'Health: {health}', pygame.font.SysFont(None, 30), (255, 255, 255), screen, 10, 10)
        draw_text(f'Speed: {alien_speed:.2f} px/s', pygame.font.SysFont(None, 30), (255, 255, 255), screen, 10, 40)
        draw_text(f'Kills: {alien_kills}', pygame.font.SysFont(None, 30), (255, 255, 255), screen, 10, 70)

        # Отрисовка количества убийств по центру экрана с прозрачностью
        kills_font = pygame.font.SysFont(None, 100)
        kills_text = kills_font.render(str(alien_kills), True, (255, 255, 255))
        kills_text.set_alpha(128)
        kills_rect = kills_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(kills_text, kills_rect)

        pygame.display.update()  # Обновление дисплея

    pygame.quit()
    sys.exit()


# Функция для завершения игры
def game_over():
    click = False  # Переменная для отслеживания кликов мыши в экране завершения игры
    while True:
        screen.blit(BACKGROUND_IMAGE, (0, 0))  # Отрисовка фона
        draw_text('Game Over', pygame.font.SysFont(None, 80), (255, 255, 255), screen, 275,
                  100)  # Текст завершения игры

        mx, my = pygame.mouse.get_pos()  # Получение текущей позиции мыши

        button_restart = pygame.Rect(325, 250, 150, 50)  # Создание кнопки перезапуска
        button_quit = pygame.Rect(325, 350, 150, 50)  # Создание кнопки выхода

        # При наведении и клике на кнопку перезапуска
        if button_restart.collidepoint((mx, my)) and click:
            game_loop()

        # При наведении и клике на кнопку выхода
        if button_quit.collidepoint((mx, my)) and click:
            pygame.quit()
            sys.exit()

        pygame.draw.rect(screen, (255, 0, 0), button_restart)  # Отрисовка кнопки перезапуска
        draw_text('Начать заново', pygame.font.SysFont(None, 30), (0, 0, 0), screen, 335,
                  260)  # Текст на кнопке перезапуска
        pygame.draw.rect(screen, (255, 0, 0), button_quit)  # Отрисовка кнопки выхода
        draw_text('Выйти', pygame.font.SysFont(None, 40), (0, 0, 0), screen, 350, 360)  # Текст на кнопке выхода

        click = False

        for event in pygame.event.get():
            # Обработка выхода из игры
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Обработка клика мыши
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True

        pygame.display.update()  # Обновление дисплея


if __name__ == "__main__":
    main_menu()  # Запуск главного меню при старте программы
