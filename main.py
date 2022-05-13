import random
from tkinter import END

start = input("Are you ready to play? Yes or No: ").lower()
DiceNum = random.randint(1, 6)
print(DiceNum)
if start == "yes":
    start2 = int(input("Guess what the computer has guessed!: ").lower())
    guess = int(DiceNum) - int(start2)
    if start2 == DiceNum:
        print("you guessed it right!")

    elif start2 != DiceNum:
        if int(guess) <= 0:
            guess = (int(start2) + int(DiceNum)) - int(start2)
            print("You are close by " + "-" + str(guess))
            start3 = int(input("What do you think the number is: "))
            if start3 == DiceNum:
                print("You guessed it right!")
            else:
                print("You failed!")
                END
        else:
            print("You are close by " + "+" + str(guess))
            start3 = int(input("What do you think the number is: "))
            if start3 == DiceNum:
                print("You guessed it right!")
            else:
                print("You failed!")
                END
    else:
        print("Error out of loop")


else:
    print("Bye, till next time.")
