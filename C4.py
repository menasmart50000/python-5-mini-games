
from rich import print as rprint


class Connect4():

    def __init__(self, width=7, height=6):

        self.width = width
        self.height = height
        self.cells = [["  "]*self.width for row in range(self.height)]
        self.score1 = 0
        self.score2 = 0
        self.Token1 = "⚫"
        self.Token2 = "⚪"

 # Helper functions begins

    def BoardDraw(self):

        guide = [str(1+i) for i in range(self.width)]
        print(guide, end="\n\n")
        for row in self.cells:
            print(row)

    def insertToken(self, num, matrix, token):
        for i in range((len(matrix)-1), -1, -1):
            if " " in matrix[i][(num-1)]:
                matrix[i][(num-1)] = token
                break
        else:
            pass

    def RowCheck(self, token):
        checker = []
        C4 = [token, token, token, token]
        counter = 0
        for row in self.cells:
            for j in range(0, 4):
                for k in range(j, j+4):
                    checker.append(row[k])
                if C4 == checker:
                    checker = []
                    return True
                checker = []
        return False

    def ColumnCheck(self, token):
        checker = []
        column = []
        C4 = [token, token, token, token]
        counter = 0

        for col in range(self.width):
            for row in range(self.height):
                column.append(self.cells[row][col])
            for col in column:
                for j in range(0, 3):
                    for k in range(j, j+4):
                        checker.append(column[k])
                    if C4 == checker:
                        checker = []
                        return True
                    checker = []
            column = []
        return False

    def DiagonalsCheck(self, token):
        diag = []
        checker = []
        C4 = [token, token, token, token]

        # checking for diagonal to the left
        for offset in range(0, 6):
            diag = [row[i+offset]
                    for i, row in enumerate(self.cells)
                    if 0 <= i+offset < len(row)]

            for j in range(0, 3):
                if j+4 > len(diag):
                    break
                else:
                    for k in range(j, j+4):
                        checker.append(diag[k])
                        if C4 == checker:
                            checker = []
                            return True
                    checker = []

            diag = []

        for offset in range(0, 6):
            diag = [row[(-i-offset)] for i, row in enumerate(self.cells)
                    if 0 > (-i-offset) >= -len(row)]

            for j in range(0, 3):
                if j+4 > len(diag):
                    break
                else:
                    for k in range(j, j+4):
                        checker.append(diag[k])
                        if C4 == checker:
                            checker = []
                            return True
                    checker = []

            diag = []

            # check for right

        pass

 # helper functions end

 # begin Game Status definition

    def winStatus(self, playerID):
        winner = f"{playerID}"
        rprint(f"[red]Connect 4![/]")
        rprint("player "+winner+" has won!")
        self.resetStatus()
        PlayAgain = input("Care to Play Again? YES:y , NO:n")
        if PlayAgain == "y":
            pass
        elif PlayAgain == "n":
            print("Thank you sure!")
            quit()

    def resetStatus(self):
        self.cells = [[" "]*self.width for row in range(self.height)]
        pass
 # end Game Status definition

    def PlayGame(self):
        user1Choice = 0
        user2Choice = 0

        while True:

            while True:
                try:
                    player1 = int(input("Player 1 to play "))
                    if player1 >= 1 and player1 <= 7:
                        user1Choice = player1
                        break
                    else:
                        rprint(
                            "enter only valid number from 1 to 7 as the guide please")

                except:
                    rprint("enter only valid number from 1 to 7 as the guide please")

            self.insertToken(user1Choice, self.cells, self.Token1)
            self.BoardDraw()

            while True:
                try:
                    player2 = int(input("Player 2 to play "))
                    if player2 >= 1 and player2 <= 7:
                        user2Choice = player2
                        break
                    else:
                        rprint(
                            "enter only valid number from 1 to 7 as the guide please")
                except:
                    print("enter only valid number from 1 to 7 as the guide please")

            self.insertToken(user2Choice, self.cells, self.Token2)
            self.BoardDraw()

            if self.RowCheck(self.Token1) or self.ColumnCheck(self.Token1) or self.DiagonalsCheck(self.Token1):
                self.winStatus(1)

            if self.RowCheck(self.Token2) or self.ColumnCheck(self.Token2) or self.DiagonalsCheck(self.Token2):
                self.winStatus(2)
