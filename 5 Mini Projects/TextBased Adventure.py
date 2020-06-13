# 4. TextBased Adventure Game
#
# The Goal: Remember Adventure? Well, we’re going to build a more basic version of that. A complete text game, the program will let users move through rooms based on user input and
# get descriptions of each room. To create this, you’ll need to establish the directions in which the user can move, a way to track how far the user has moved (and therefore which room he/she is in),
# and to print out a description. You’ll also need to set limits for how far the user can move. In other words, create “walls” around the rooms that tell the user, “You can’t move further in this direction.”
# Concepts to keep in mind:
#
# Strings
# Variables
# Input/Output
# If/Else Statements
# Print
# List
# Integers
#
# The tricky parts here will involve setting up the directions and keeping track of just how far the user has “walked” in the game. I suggest sticking to just a few basic descriptions or rooms, perhaps 6 at most.
# This project also continues to build on using userinputted data. It can be a relatively basic game, but if you want to build this into a vast, complex word, the coding will get substantially harder, especially if
# you want your user to start interacting with actual objects within the game. That complexity could be great, if you’d like to make this into a longterm project. *Hint hint.

import time
import textLines as txtLns


def main():
    print("Welcome to Cosmin's Python Adventure Game!\n")
    print("""How to play:
The actions you take in this game are based on what the input you give it are,
so if you are given the choice to go to the left or the right, typing with the keyword "left" or "right" will execute
that action, for example typing out \"the door to the left\", \"I go to the left\", or other such phrases.\n""")

    time.sleep(3)

    print("""You find yourself in an empty, windowless room with a single lighting fixture on the ceiling,
illuminating a clean hardwood floor, white plaster walls,\nas well as a door to your left and to your right\n""")



#     print("""How to play:
# The actions you take in this game are based on what the input you give it are,
# so if you are given the choice to go to the left or the right, typing with the keyword "left" or "right" will execute
# that action, for example typing out \"the door to the left\", \"I go to the left\", or other such phrases.""")
    answer = ""
    while answer != "left" or answer != "right":
        print("What would you like to do, go through the door on the left, or the door on the right?\n")
        answer = input((""))
        answer = answer.lower()
        if "left" in answer:
            answer += "left"
            room1()
            break


        if "right" in answer:
            answer += "right"
                # room2()
            break


def room1():
    # This is the room with bookshelves in it
    print("\n" + txtLns.line2)
    print(txtLns.line3)
    print("What do you do next?\n")
    answer = input("")
    while answer != "back" or answer != "right":
        if "right" in answer:
            # room3()
            print("room3")
            break
        if "back" in answer:
            # room0()
            print("room1")
            break
        # if
main()

