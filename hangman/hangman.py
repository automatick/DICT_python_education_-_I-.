from random import choice
from string import ascii_lowercase

print("HANGMAN")

def game():

    words: list = ["python", "java", "php", "javascript"]
    random_word: list = choice(words)
    guess: str = "-" * len(random_word)
    attempts: int = 8
    dontAppear: bool = False
    noImprove: bool = False
    usedLetters: list[str] = []
    singleLetter: bool = True
    notEng: bool = False
    duplicate: bool = False
    
    while True:
        print("\033[H\033[J" + guess)
        
        if dontAppear:
            print("That letter doesn't appear in the word")
            dontAppear = False
        elif noImprove:
            print("No improvements")
            noImprove = False
        elif not singleLetter:
            print("You should input a single letter.")
            singleLetter = True
        elif notEng:
            print("Please enter the lovercase english letter!")
            notEng = False
        elif duplicate:
            print("You already use this letter!")
            duplicate = False
            
        letter: str
        if (letter := input("Input a letter -> ")) == "":
            continue
        elif len(letter) != 1:
            singleLetter = False
            continue
        elif letter in usedLetters:
            duplicate = True
            continue

        usedLetters.append(letter)

        if letter not in ascii_lowercase:
            notEng = True
            continue

        correct: bool = False
        for i, l in enumerate(random_word):
            if letter == guess[i]:
                noImprove = True
                break
            if l == letter:
                correct = True
                if 0 <= i < len(guess):
                    guess = guess[:i] + letter + guess[i + 1 :]

        if noImprove:
            continue

        if not correct:
            attempts -= 1
            dontAppear = True
            if attempts == 0:
                print("You lost")
                break

        if "-" not in guess and attempts >= 1:
            print("\033[H\033[J" + f"You won. Correct word is {guess}")
            break

if __name__ == "__main__":
    action: str = input("Type 'play' to play the game, 'exit' to quit: -> ")
    while action != 'exit':
        if action == 'play':
            game()
        else:
            print('Incorect action!')
        action: str = input("Type 'play' to play the game, 'exit' to quit: -> ")
