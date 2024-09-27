#consts
BOT_NAME = "idk"
CREATION_YEAR = "2024"

#vars
usr_name = ""
age = 0
numbers = 0
answ = ""

print (
    f"""Hello! My name is {BOT_NAME}
I was created in {CREATION_YEAR}
Please remind me your name.
    """
)

usr_name = input("-> ")

while True:
    print (
        f"What a great name you have, {usr_name}! \nEnter remainders of dividing your age by 3, 5 and 7."
    )
    try:
        rem3, rem5, rem7 = map(int, [input("-> ").replace(" ", ""), input("-> ").replace(" ", ""), input("-> ").replace(" ", "")])
        break
    except ValueError:
        print("Too much or enougth values, please check it!")

age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

print (
    f"Your age is {age}; that's a good time to start programming!\nNow I will prove to you that I can count to any number you want."
)

numbers = int(input("-> "))

print (
    "!\n".join(map(str, range(numbers + 1))), end="!\n"
)

print (
"""
Let's test your programming knowledge.
Why do we use methods?
1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.
"""
)

answ = input("-> ")


while answ != "2":
    print("Please, try again.")
    answ = input("-> ")

print("Completed, have a nice day! \nCongratulations, have a nice day!")
