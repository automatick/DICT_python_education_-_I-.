import sys
import random

count: int = int(input("Enter the number of friends joining (including you): -> "))
friends: dict[str, int] = {}

if count < 0:
    print("Incorrect number")
    sys.exit()
elif count == 0:
    print("No one joined the party:(")
    sys.exit()

print("Enter the name of every friend (including you), each on a new line:")


def fill() -> dict:
    friends_dict = {}
    for i in range(count):
        friends_dict[input("-> ")] = 0
    return friends_dict

friends = fill()
amount: int = int(input("Enter a total ammount -> "))
amountForOne: int = 0

amountForOne = round( amount / len(friends), 2 )

for i in friends:
    friends[i] = amountForOne

lucky: bool = True if input('Do you want to use the "Who is lucky?" feature? Write Yes/No -> ').lower() == 'yes' else False

if lucky:
    luckyPerson: str = random.choice(list(friends.keys()))
    friends[luckyPerson] = 0
    print(f"{luckyPerson} is the lucky one!")
else:
    print(friends)
    sys.exit()

newAmountForOne: int = round( amount / (len(friends) - 1), 2 )

for i in friends.keys():
    if i != luckyPerson: friends[i] = newAmountForOne

print(friends)
