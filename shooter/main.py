import pygame
from game import Game

pygame.init()

game = Game()
game.run()

pygame.quit()

для
обучения
опиши
мне
все
возможные
варианты
применения

try ecsept

    с
примерfми
и
метафорами
для
конспектирования
на
англ, французском
и
рус


# Examples provided demonstrate various scenarios where try-except can be used to handle errors effectively,
# making the code more robust and reliable.
# Приведенные примеры демонстрируют различные сценарии, где try-except можно использовать для эффективной обработки ошибок,
# делая код более надежным.



from art import logo, vs
from game_data import adata
import random

print(logo)
A = {}
B = {}
score = 0

def chouse_a_b():
    # Globa; Scope
    global A
    A = [random.choice(adata) for i in range(1)]
    A = A[0]
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
    print(vs)
    global B
    B = [random.choice(adata) for i in range(1)]
    B = B[0]
    print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}")


def compare():
    chouse_a_b()
    global A
    global B
    global Run
    global score
    guess = (input("Who has more followers? Type 'A' or 'B': ")).lower()

    if guess == "a":
        guess = A['follower_count']
        B = B['follower_count']
        if guess > B:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            Run = False
            print(f"Sorry, that's wrong. Final score: {score}")

    if guess == "b":

        guess = B['follower_count']
        A = A['follower_count']
        if guess > A:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            Run = False


Run = True

while Run:
    compare()
    print("----------------------------------------------")