from random import randint


def RPS():
    score = 0
    comp_score = 0

    names = {1: "rock", 2: "paper", 3: "scissor"}

    while True:
        try:
            scoreLimit = int(input("enter the score limit: "))
            if True:
                break
        except:
            print("enter a valid score limit")

    while True:
        comp = randint(1, 3)
        try:
            user = input("choose your intety: ")
            if user in names:
                pass
        except:
            print("please enter one of those words : rock, paper,scissor ")

        if user == names[2] and names[comp] == names[1]:
            print("you won!")
            score += 1
        elif user == names[1] and names[comp] == names[3]:
            print("you won!")
            score += 1
        elif user == names[3] and names[comp] == names[2]:
            print("you won!")
            score += 1
        else:
            print("you lose that time!")
            comp_score += 1
        if score == scoreLimit:
            print("Congratulation, you won!")
            PlayAgain = input("Care to Play Again? YES:y , NO:n ")
            if PlayAgain == "y":
                pass
            elif PlayAgain == "n":
                print("Thank you for playing sure!")
                break

        elif comp_score == scoreLimit:
            print("Ahh I got you this Time! I WIN YOU LOSE ")
            PlayAgain = input("Care to Play Again? YES:y , NO:n ")
            if PlayAgain == "y":
                pass
            elif PlayAgain == "n":
                print("Thank you for playing sure!")
                break
