import random

print("To get a number to guess, please type the number you want to limit to:")
limit = input("-")

number = random.randrange(1, int(limit))
print(number)
print("Now it is time to guess the random number that is between 1 and {}".format(limit))
guess = 0
userValue = 0

while True:
    print("Take a guess:")
    userValue = input()
    if int(userValue) == number:
        print("You got it right!")
        break
    else:
        print("Try again!")