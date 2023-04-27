import random


def GuessTheNumber(y):

    number = random.randint(0, y)
    while True:

        while True:
            try:
                user = float(input("guess your Number!"))
                if True:
                    break
            except:
                print("please enter a number")

        if user == number:
            print("you won!")
            PlayAgain = input("Care to Play Again? YES:y , NO:n")
            if PlayAgain == "y":
                number = random.randint(0, y)
                pass
            elif PlayAgain == "n":
                print("Thank you sure!")
                break

        elif user < number:
            print("Hmmmm, Too low, give it another shot!")
        else:
            print("Hmmmm, Too HIGH, give it another shot!")
