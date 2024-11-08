class CoffeeMachine:
    def __init__(self):
        # Ініціалізація початкових значень
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.cups = 9
        self.money = 550
        self.state = 'waiting_for_action'

    def handle_input(self, action):
        # Обробка вводу залежно від поточного стану
        if self.state == 'waiting_for_action':
            self.process_action(action)
        elif self.state == 'choosing_coffee':
            self.process_coffee_choice(action)
        elif self.state == 'filling':
            self.process_fill(action)

    def process_action(self, action):
        # Обробка команд користувача в основному меню
        if action == 'buy':
            self.state = 'choosing_coffee'
            print("Що ви хочете купити? 1 - еспресо, 2 - латте, 3 - капучино, back - до головного меню:")
        elif action == 'fill':
            self.state = 'filling'
            self.fill_stage = 0
            print("Напишіть, скільки мл води ви хочете додати:")
        elif action == 'take':
            print(f"Я дав вам ${self.money}")
            self.money = 0
        elif action == 'remaining':
            self.show_remaining()
        elif action == 'exit':
            exit()
        else:
            # Невірна команда
            print("Невірна дія. Спробуйте ще раз.")

    def process_coffee_choice(self, choice):
        # Обробка вибору кави
        if choice == '1':
            self.make_coffee(250, 0, 16, 4)
        elif choice == '2':
            self.make_coffee(350, 75, 20, 7)
        elif choice == '3':
            self.make_coffee(200, 100, 12, 6)
        elif choice == 'back':
            self.state = 'waiting_for_action'
        else:
            # Невірний вибір
            print("Невірний вибір. Спробуйте ще раз.")

    def make_coffee(self, water, milk, coffee, price):
        # Створення кави залежно від наявних ресурсів
        if self.water < water:
            print("Вибачте, недостатньо води!")
        elif self.milk < milk:
            print("Вибачте, недостатньо молока!")
        elif self.coffee_beans < coffee:
            print("Вибачте, недостатньо кавових зерен!")
        elif self.cups < 1:
            print("Вибачте, недостатньо одноразових чашок!")
        else:
            print("У мене достатньо ресурсів, готую каву!")
            self.water -= water
            self.milk -= milk
            self.coffee_beans -= coffee
            self.cups -= 1
            self.money += price
        self.state = 'waiting_for_action'

    def process_fill(self, amount):
        # Обробка введення кількості додаваних ресурсів
        try:
            amount = int(amount)
        except ValueError:
            print("Будь ласка, введіть число!")
            return

        stages = ["води", "молока", "кавових зерен", "одноразових чашок"]
        amounts = [self.water, self.milk, self.coffee_beans, self.cups]
        amounts[self.fill_stage] += amount
        self.fill_stage += 1

        if self.fill_stage < len(stages):
            print(f"Напишіть, скільки {stages[self.fill_stage]} ви хочете додати:")
        else:
            self.state = 'waiting_for_action'

    def show_remaining(self):
        # Показати наявні ресурси
        print("У кавоварці залишилось:")
        print(f"{self.water} мл води")
        print(f"{self.milk} мл молока")
        print(f"{self.coffee_beans} г кавових зерен")
        print(f"{self.cups} одноразових чашок")
        print(f"{self.money} доларів")

# Приклад використання
machine = CoffeeMachine()
while True:
    action = input("Введіть дію (buy, fill, take, remaining, exit): ")
    machine.handle_input(action)
