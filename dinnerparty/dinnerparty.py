import sys

count: int = int(input("Enter the number of friends joining (including you): -> "))
friends: dict = {}

if count < 0:
    print("Incorrect number")
    sys.exit()
elif count == 0:
    print("No one joined the party:(")

print("Enter the name of every friend (including you), each on a new line:")

for i in range(count):
    friends[input("-> ")] = 0

amount: int = int(input("Enter a total ammount -> "))
amountForOne: int = 0

amountForOne = round( amount / len(friends), 2 )

for i in friends:
    friends[i] = amountForOne

print(friends)
