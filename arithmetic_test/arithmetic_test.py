import random  # Імпортуємо модуль для генерації випадкових чисел

def generate_question(level):
    """
    Генерує арифметичне завдання залежно від рівня складності.
    Рівень 1: арифметичні операції з числами від 2 до 9.
    Рівень 2: зведення у квадрат чисел від 11 до 29.
    """
    if level == 1:
        num1, num2 = random.randint(2, 9), random.randint(2, 9)
        operation = random.choice(['+', '-', '*'])
        question = f"{num1} {operation} {num2}"
        answer = eval(question)  # Обчислення правильної відповіді
    elif level == 2:
        num = random.randint(11, 29)
        question = f"{num}"
        answer = num ** 2  # Обчислення квадрата числа
    return question, answer

def get_valid_input():
    """
    Отримує введене користувачем число та перевіряє його формат.
    Якщо формат неправильний (літери, порожній ввід), виводить "Incorrect format." і просить повторити.
    """
    while True:
        user_input = input("> ")
        if user_input.lstrip('-').isdigit():  # Перевіряємо, чи це число (може бути від'ємним)
            return int(user_input)
        print("Incorrect format.")

def main():
    """
    Основна функція програми. Запитує рівень складності, проводить тест з 5 питань,
    підраховує правильні відповіді та (за бажанням користувача) зберігає результат у файл.
    """
    
    # Вибір рівня складності
    print("Which level do you want? Enter a number:")
    print("1 - simple operations with numbers 2-9")
    print("2 - integral squares of 11-29")

    while True:
        level_input = input("> ")
        if level_input in ('1', '2'):
            level = int(level_input)
            break
        print("Incorrect format.")

    correct_answers = 0  # Лічильник правильних відповідей

    # Проведення тесту з 5 питань
    for _ in range(5):
        question, correct_answer = generate_question(level)  # Генеруємо питання та правильну відповідь
        print(question)
        user_answer = get_valid_input()  # Отримуємо відповідь користувача

        if user_answer == correct_answer:
            print("Right!")
            correct_answers += 1
        else:
            print("Wrong!")

    # Виведення підсумкового результату
    print(f"Your mark is {correct_answers}/5.")

    # Пропозиція збереження результату у файл
    save_result = input("Would you like to save your result to the file? Enter yes or no.\n> ").strip().lower()
    if save_result in ("yes", "y"):
        username = input("What is your name?\n> ")
        level_desc = "simple operations with numbers 2-9" if level == 1 else "integral squares of 11-29"
        result_entry = f"{username}: {correct_answers}/5 in level {level} ({level_desc})\n"

        # Запис у файл
        with open("results.txt", "a") as file:
            file.write(result_entry)

        print('The results are saved in "results.txt".')

if __name__ == "__main__":
    main()

