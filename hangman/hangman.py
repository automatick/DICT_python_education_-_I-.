from random import choice

print("HANGMAN")

words: list = ["python", "java", "php", "javascript"]
random_word: list = choice(words)
guess: str = "-" * len(random_word)
attempts: int = 8

while True:
    print(guess)
    letter: str = input("Input a letter -> ")[0]
    correct: bool = False
    for i in range(len(random_word)):
        if random_word[i] == letter:
            correct = True
            if 0 <= i < len(guess):
                guess = guess[:i] + letter + guess[i + 1:]
    if not correct:
        attempts -= 1
        print("That letter doesn't appear in the word")
        if attempts == 0:
            print("You lost")
            break
    if "-" not in guess:
        print("You won")
        break
