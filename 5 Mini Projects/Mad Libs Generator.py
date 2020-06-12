# 3. Mad Libs Generator
#
# The Goal: Inspired by Summer Son’s Mad Libs project with Javascript. The program will first prompt the user for a
# series of inputs a la Mad Libs. For example, a singular noun, an adjective, etc. Then, once all
# the information has been inputted, the program will take that data and place them into a pre-made story template.
# You’ll need prompts for user input, and to then print out the full story at the end with the input included.
# Concepts to keep in mind:
#
# Strings
# Variables
# Concatenation
# Print
#
# A pretty fun beginning project that gets you thinking about how to manipulate user inputted data. Compared to the prior
# projects, this project focuses far more on strings and concatenating. Have some fun coming up with some wacky stories
# for this!


def main():

    while True:
        print("Welcome to Mad Libs! Would you like story 1, 2, or 3?")
        selection = int(input())
        if selection == 1:
            print("Story 1")
            story1()
        elif selection == 2:
            print("Story 2")
            # story2()
        elif selection == 3:
            print("Story 3")
            # story3()
        break


def story1():
    line1 = "While {verb1} the other day, you noticed a {adjective1} {noun1} walking at a speed of {number1}km per hour."
    print(line1.format(verb1 = "(a Verb)", adjective1 = "(a Silly Adjective)", noun1 = "(a Noun involving travel)", number1 = "(a crazy number)"))
    print("Now to fill them in! Follow the prompts given, seperating each one with a comma, like in the following example: seven, 8, blue, tall, running.")
    list1 = []
    list1 += input("")
    print(list1)
    print(line1.format(verb1 = list1[0], adjective1 = list1[1], noun1 = list1[2], number1 = list1[3]))

main()