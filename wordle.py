from rich import print
import random
import os


# reading from wordlist file
wordlist = []
with open('wordle/wordlist.txt', mode="r") as wordGenerator:
    wordlist = wordGenerator.readlines()

for i, word in enumerate(wordlist):
    wordlist[i] = word.strip('\n')


class wordle():
    def __init__(self):
        self.limit = 5
        self.words = random.choice(wordlist)
        self.guessNum = 0
        self.cells = {
            0: [""]*5,
            1: [""]*5,
            2: [""]*5,
            3: [""]*5,
            4: [""]*5,
            5: [""]*5

        }

    def resetStatus(self):
        self.words = random.choice(wordlist)
        self.guessNum = 0
        self.cells.popitem
        self.cells = {
            0: [""]*5,
            1: [""]*5,
            2: [""]*5,
            3: [""]*5,
            4: [""]*5,
            5: [""]*5


        }

    def draw(self):
        for cell in self.cells.values():
            print(" | ".join(cell))
            print("==================")

    def getUserInput(self):
        while True:
            user = input("enter 5letter word ")
            if len(user) == 5:
                break
            else:
                print("please enter 5 letter word ")
        return user

    def playGame(self):

        while True:
            userInput = self.getUserInput()
            compChoice = self.words

            for i in range(len(userInput)):

                if (userInput[i] in compChoice) and (userInput[i] == compChoice[i]):
                    char = userInput[i]
                    char = char = f"[green]{char}[/]"
                    self.cells[self.guessNum][i] = char = char

                elif (userInput[i] in compChoice):
                    pchar = userInput[i]
                    pchar = f"[yellow]{pchar}[/]"
                    self.cells[self.guessNum][i] = pchar
                else:
                    self.cells[self.guessNum][i] = userInput[i]

            if userInput == compChoice:
                self.draw()
                print("congrats, thats the right word, you won!")

                self.resetStatus()
                PlayAgain = input("Care to Play Again? YES:y , NO:n")
                if PlayAgain == "y":
                    pass
                elif PlayAgain == "n":
                    print("Thank you sure!")
                    break

            elif userInput != compChoice:
                self.draw()
                self.guessNum += 1
                print("Wrong guess try again")

            if self.guessNum > self.limit:
                print("sorry man, you lose! the word was: " + compChoice)
                self.resetStatus()
                PlayAgain = input("Care to Play Again? YES:y , NO:n")
                if PlayAgain == "y":
                    pass
                elif PlayAgain == "n":
                    print("Thank you sure!")
                    break
