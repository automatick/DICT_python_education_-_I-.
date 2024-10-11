import random

print("HANGMAN")
words: list = ["python", "java", "php", "javascript"]

random_word: list = random.choice(words)

if input(f"Guess the word {random_word[:3] + (len(random_word) - 3) * '-'} -> ") == random_word:
    print("you survived")

else:
    print("you dead")
