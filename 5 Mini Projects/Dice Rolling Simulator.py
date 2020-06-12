from random import randrange
rollRequest = ""
while rollRequest != "end" :
    rollRequest = (input("Type 'roll' to roll!\nTyping 'end' will end the rolling of the dice\n"))
    if rollRequest == "roll":
        print("You rolled a " + str(randrange(1, 6)) +"!" )
    else:
        print("Thanks for rolling!")