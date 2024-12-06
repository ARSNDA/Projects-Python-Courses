# Меню кофемашины с описанием ингредиентов и стоимости для каждого напитка
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "milk": 100,
            "water": 250,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Исходные ресурсы машины
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# Функция для вывода текущих ресурсов
def check_resource():
    for position, resource in resources.items():
        print(f"{position} = {resource}")


# Функция для обновления ресурсов до начальных значений
def update():
    new_resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
    for position, amount in new_resources.items():
        resources[position] = amount
        print(f"{position} = {resources[position]}")


# Проверка наличия достаточных ресурсов для приготовления выбранного напитка
def sufficient_resources(ingredients):
    for item in ingredients:
        if ingredients[item] > resources.get(item, 0):
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# Вычитание нужного количества ингредиентов из ресурсов после приготовления напитка
def subtract_resources(ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]


# Обработка монет и проверка достаточности средств для покупки напитка
def process_coins(cost):
    quarters = int(input("How many quarters? "))  # Запрос русских монет
    dimes = int(input("How many dimes? "))  # Запрос копеек
    nickels = int(input("How many nickels? "))  # Запрос пятаков
    pennies = int(input("How many pennies? "))  # Запрос пенни
    total = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01

    if total < cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    elif total > cost:
        change = round(total - cost, 2)
        print(f"Here is ${change} in change.")

    print("Transaction successful!")
    return True


# Основная функция для запроса выбора пользователя
def user_choice():
    off = True

    while off:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if choice == "report":
            check_resource()  # Отчет о текущих ресурсах
        elif choice == 'update':
            update()  # Обновление ресурсов
        elif choice == 'off':
            print("Turning off the coffee machine.")  # Отключение машины
            off = False
        elif choice in MENU:
            if sufficient_resources(MENU[choice]["ingredients"]):
                if process_coins(MENU[choice]["cost"]):
                    subtract_resources(MENU[choice]["ingredients"])
                    print(f"Here is your {choice}. Enjoy!")
                else:
                    print(f"Sorry, unable to prepare {choice}.")
            else:
                print(f"Sorry, unable to prepare {choice}.")
        else:
            print("Invalid choice. Please try again.")  # Некорректный ввод


# Запуск функции выбора пользователя
user_choice()









del resources["milk"]  # Удаляет молоко из ресурсов
