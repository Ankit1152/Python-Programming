import random
cNumber = random.randrange(1,101)
userInput = int(input("Enter your number--"))

if cNumber > userInput:
    print("Computer generated Number ",cNumber)
    print("Your guess number is small")
elif cNumber < userInput:
    print("Computer generated Number ",cNumber)
    print("Your guess number is large")
else:
    print("Computer generated Number ",cNumber)
    print("your guess number is equal")