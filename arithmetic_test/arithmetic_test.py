import random  # Імпортуємо модуль для генерації випадкових чисел

def generate_question(level):
    """
    Генерує арифметичне завдання залежно від рівня складності.
    """
    if level == 1:
        return generate_simple_operation()
    elif level == 2:
        return generate_square_question()

def generate_simple_operation():
    """
    Генерує арифметичну операцію з числами від 2 до 9.
    """
    num1, num2 = random.randint(2, 9), random.randint(2, 9)
    operation = random.choice(['+', '-', '*'])
    question = f"{num1} {operation} {num2}"
    answer = eval(question)  # Обчислення правильної відповіді
    return question, answer

def generate_square_question():
    """
    Генерує завдання на зведення у квадрат числа від 11 до 29.
    """
    num = random.randint(11, 29)
    return f"{num}", num ** 2  # Обчислення квадрата числа

def get_valid_input():
    """
    Отримує введене користувачем число та перевіряє його формат.
    """
    while True:
        user_input = input("> ")
        if user_input.lstrip('-').isdigit():  # Перевіряємо, чи це число (може бути від'ємним)
            return int(user_input)
        print("Incorrect format.")

def choose_level():
    """
    Запитує у користувача рівень складності.
    """
    print("Which level do you want? Enter a number:")
    print("1 - simple operations with numbers 2-9")
    print("2 - integral squares of 11-29")

    while True:
        level_input = input("> ")
        if level_input in ('1', '2'):
            return int(level_input)
        print("Incorrect format.")

def ask_questions(level, num_questions=5):
    """
    Проводить тест із вказаною кількістю питань та повертає кількість правильних відповідей.
    """
    correct_answers = 0

    for _ in range(num_questions):
        question, correct_answer = generate_question(level)  # Генеруємо питання та відповідь
        print(question)
        user_answer = get_valid_input()  # Отримуємо відповідь користувача

        if user_answer == correct_answer:
            print("Right!")
            correct_answers += 1
        else:
            print("Wrong!")

    return correct_answers

def save_result(username, correct_answers, level):
    """
    Зберігає результат у файл results.txt.
    """
    level_desc = "simple operations with numbers 2-9" if level == 1 else "integral squares of 11-29"
    result_entry = f"{username}: {correct_answers}/5 in level {level} ({level_desc})\n"

    with open("results.txt", "a") as file:
        file.write(result_entry)

    print('The results are saved in "results.txt".')

def main():
    """
    Основна функція програми.
    """
    level = choose_level()  # Вибір рівня
    correct_answers = ask_questions(level)  # Проведення тесту

    print(f"Your mark is {correct_answers}/5.")

    # Пропозиція збереження результату
    save_result_choice = input("Would you like to save your result to the file? Enter yes or no.\n> ").strip().lower()
    if save_result_choice in ("yes", "y"):
        username = input("What is your name?\n> ")
        save_result(username, correct_answers, level)

if __name__ == "__main__":
    main()
