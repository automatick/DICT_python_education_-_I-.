import random

def get_initial_pencils():
    while True:
        pencils = input("How many pencils would you like to use:\n")
        if not pencils.isdigit():
            print("The number of pencils should be numeric")
        elif int(pencils) <= 0:
            print("The number of pencils should be positive")
        else:
            return int(pencils)

def get_first_player(name1, name2):
    while True:
        first = input(f"Who will be the first ({name1}, {name2}):\n")
        if first not in [name1, name2]:
            print(f"Choose between '{name1}' and '{name2}'")
        else:
            return first

def bot_move(pencils):
    if pencils % 4 == 0:
        return 3
    elif pencils % 4 == 3:
        return 2
    elif pencils % 4 == 2:
        return 1
    else:
        return random.choice([1, 2, 3])

def game():
    pencils = get_initial_pencils()
    name1 = "John"
    name2 = "Jack"  # Bot
    current_player = get_first_player(name1, name2)

    while pencils > 0:
        print('|' * pencils)
        print(f"{current_player}'s turn!")

        if current_player == name2:
            move = bot_move(pencils)
            print(move)
        else:
            while True:
                move = input()
                if not move.isdigit() or int(move) not in [1, 2, 3]:
                    print("Possible values: '1', '2' or '3'")
                elif int(move) > pencils:
                    print("Too many pencils were taken")
                else:
                    move = int(move)
                    break

        pencils -= move
        current_player = name1 if current_player == name2 else name2

    print(f"{current_player} won!")

if __name__ == "__main__":
    game()
