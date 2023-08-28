def number_to_word():
    try:
        userInput = int(input("Enter a number from 1-10: "))
        if userInput == 1:
            print("You Just Entered One")
        elif userInput == 2:
            print("You Just Entered Two")
        elif userInput == 3:
            print("You Just Entered Three")
        elif userInput == 4:
            print("You Just Entered Four")
        elif userInput == 5:
            print("You Just Entered Five")
        elif userInput == 6:
            print("You Just Entered Six")
        elif userInput == 7:
            print("You Just Entered Seven")
        elif userInput == 8:
            print("You Just Entered Eight")
        elif userInput == 9:
            print("You Just Entered Nine")
        elif userInput == 10:
            print("You Just Entered Ten")
        else:
            print("Invalid Input :(")
            number_to_word()
    except ValueError:
        print("Enter a number!!")


number_to_word()
