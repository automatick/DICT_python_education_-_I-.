# Етап 1: Симуляція процесу приготування кави
def make_coffee():
    print("Starting to make a coffee")
    print("Grinding coffee beans")
    print("Boiling water")
    print("Mixing boiled water with crushed coffee beans")
    print("Pouring coffee into the cup")
    print("Pouring some milk into the cup")
    print("Coffee is ready!")

# Етап 2: Розрахунок кількості інгредієнтів для необхідної кількості чашок
def calculate_ingredients(n_cups):
    # Одна чашка потребує: 200 мл води, 50 мл молока, 15 г кавових зерен
    water_per_cup = 200
    milk_per_cup = 50
    coffee_per_cup = 15
    
    total_water = water_per_cup * n_cups
    total_milk = milk_per_cup * n_cups
    total_coffee = coffee_per_cup * n_cups
    
    print(f"For {n_cups} cups of coffee you will need:")
    print(f"{total_water} ml of water")
    print(f"{total_milk} ml of milk")
    print(f"{total_coffee} g of coffee beans")

# Етап 3: Доступні інгредієнти та перевірка їх достатності
def check_ingredients(available_water, available_milk, available_coffee, n_cups):
    water_per_cup = 200
    milk_per_cup = 50
    coffee_per_cup = 15
    
    required_water = water_per_cup * n_cups
    required_milk = milk_per_cup * n_cups
    required_coffee = coffee_per_cup * n_cups

    # Перевірка чи достатньо інгредієнтів для вказаної кількості чашок
    can_make_all_cups = (available_water // water_per_cup, available_milk // milk_per_cup, available_coffee // coffee_per_cup)
    possible_cups = min(can_make_all_cups)
    
    if possible_cups >= n_cups:
        extra_cups = possible_cups - n_cups
        if extra_cups > 0:
            print(f"Yes, I can make that amount of coffee (and even {extra_cups} more than that)")
        else:
            print("Yes, I can make that amount of coffee")
    else:
        print(f"No, I can make only {possible_cups} cups of coffee")

# Основна функція для запитів та запуску інших функцій
def coffee_machine():
    print("Write how many cups of coffee you will need:")
    n_cups = int(input("> "))
    
    # Розрахунок інгредієнтів
    calculate_ingredients(n_cups)
    
    # Запит наявних інгредієнтів
    print("Enter available water (in ml):")
    available_water = int(input("> "))
    
    print("Enter available milk (in ml):")
    available_milk = int(input("> "))
    
    print("Enter available coffee beans (in grams):")
    available_coffee = int(input("> "))
    
    # Перевірка, чи достатньо інгредієнтів
    check_ingredients(available_water, available_milk, available_coffee, n_cups)

# Виклик кавомашини
coffee_machine()
