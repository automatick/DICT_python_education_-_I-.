# Функція для обробки приготування кави
def make_coffee(drink_type):
    print("\nStarting to make a coffee")
    print("Grinding coffee beans")  # Мелемо кавові зерна
    print("Boiling water")  # Кип'ятимо воду
    print("Mixing boiled water with crushed coffee beans")  # Змішуємо каву з кип'яченою водою

    if drink_type in ['latte', 'cappuccino']:
        print("Pouring some milk into the cup")  # Додаємо молоко

    print("Pouring coffee into the cup")  # Наливаємо каву до чашки
    print("Coffee is ready!")  # Кава готова!

# Функція для підрахунку інгредієнтів на основі типу напою та кількості чашок
def calculate_ingredients(drink_type, cups):
    # Різні пропорції для еспресо, латте та капучіно
    if drink_type == 'espresso':
        water = 250 * cups  # Еспресо потребує 250 мл води
        milk = 0  # Без молока
        coffee_beans = 16 * cups  # 16 г кавових зерен
    elif drink_type == 'latte':
        water = 350 * cups  # Латте потребує 350 мл води
        milk = 75 * cups  # 75 мл молока
        coffee_beans = 20 * cups  # 20 г кавових зерен
    elif drink_type == 'cappuccino':
        water = 200 * cups  # Капучіно потребує 200 мл води
        milk = 100 * cups  # 100 мл молока
        coffee_beans = 12 * cups  # 12 г кавових зерен
    else:
        raise ValueError("Invalid coffee type specified!")  # Перехоплення неправильно введеного типу кави

    return water, milk, coffee_beans

# Функція для перевірки доступних інгредієнтів із додатковою обробкою помилок
def check_resources(drink_type, available_water, available_milk, available_coffee, cups_needed):
    try:
        required_water, required_milk, required_coffee = calculate_ingredients(drink_type, cups_needed)
    except ValueError as e:
        print(str(e))
        return

    # Перевіряємо чи достатньо інгредієнтів для приготування потрібної кількості кави
    if available_water >= required_water and available_milk >= required_milk and available_coffee >= required_coffee:
        extra_cups = min(available_water // required_water, available_milk // required_milk, available_coffee // required_coffee) - cups_needed
        if extra_cups > 0:
            print(f"Yes, I can make that amount of coffee (and even {extra_cups} more than that).")
        else:
            print("Yes, I can make that amount of coffee.")
    else:
        max_cups = min(available_water // (required_water // cups_needed), 
                       available_milk // (required_milk // cups_needed), 
                       available_coffee // (required_coffee // cups_needed))
        print(f"No, I can make only {max_cups} cups of coffee.")

# Функція для безпечного введення цілих чисел із перевіркою на помилки
def safe_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")  # Повідомлення про помилку, якщо введено некоректне значення

# Основна програма для взаємодії з користувачем
if __name__ == "__main__":
    try:
        # Безпечне введення кількості інгредієнтів
        available_water = safe_integer_input("Write how many ml of water the coffee machine has: ")
        available_milk = safe_integer_input("Write how many ml of milk the coffee machine has: ")
        available_coffee = safe_integer_input("Write how many grams of coffee beans the coffee machine has: ")
        cups_needed = safe_integer_input("Write how many cups of coffee you will need: ")

        # Перевіряємо чи достатньо ресурсів
        drink_type = input("Choose coffee type (espresso/latte/cappuccino): ").strip().lower()
        
        if drink_type not in ['espresso', 'latte', 'cappuccino']:
            raise ValueError("Invalid coffee type! Please choose espresso, latte or cappuccino.")
        
        check_resources(drink_type, available_water, available_milk, available_coffee, cups_needed)
        
        # Якщо можна, готуємо каву
        make_coffee(drink_type)

    except ValueError as e:
        print(f"Error: {e}")  # Обробляємо помилки неправильного вибору типу кави
    except Exception as e:
        print(f"Unexpected error: {e}")  # Інші можливі системні помилки