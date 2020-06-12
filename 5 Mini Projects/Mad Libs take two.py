def main():
    print("Mad libs generator!\n")
    line1 = "While {} the other day, you noticed a {} {} whizzing by your lawn at a speed of {} km per hour."

    wordlist1 = ["(a noun)", "(an adjective)", "(a verb)", "(a number)"]

    print(line1.format(wordlist1[2], wordlist1[0], wordlist1[1], wordlist1[3]))

    wordList2 = []

    print("Let's fill in the blanks!")
    print("What's a verb you could do in front of the house?")
    input1 = input("")
    print("What is a silly noun that could be on the sidewalk or road?")
    input2 = input("")
    print("Write a verb that silly noun could be doing.")
    input3 = input("")
    print("What is a crazy speed they could be doing that action at?")
    input4 = input("")

    wordList2.append(input1)
    wordList2.append(input2)
    wordList2.append(input3)
    wordList2.append(input4)


    print(wordList2)
    print("Let's see what that leaves us with!")
    print(line1.format(wordList2[2], wordList2[0], wordList2[1], wordList2[3]))




main()