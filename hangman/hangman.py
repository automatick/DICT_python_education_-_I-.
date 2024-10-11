import random

print("HANGMAN")
words: list = ["python", "java", "c"]
if input("Guess the word -> ") == random.choice(words):
    print("you survived")
    exit(0)
print("you dead")
