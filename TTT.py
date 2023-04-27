from rich import print as rprint


class TicTacToe():
    def __init__(self, width=3, height=3):

        self.Token1 = "X"
        self.Token2 = "O"
        self.cells = [["1", "2", "3"],
                      ["4", "5", "6"],
                      ["7", "8", "9"]]

    # Game Definition

    def winStatus(self, playerID):
        winner = f"{playerID}"
        rprint(f"[red]Tic Tac Toe![/]")
        rprint("player "+winner+" has won!")
        self.resetStatus()
        PlayAgain = input("Care to Play Again? YES:y , NO:n")
        if PlayAgain == "y":
            pass
        elif PlayAgain == "n":
            print("Thank you sure!")
            quit()

    def resetStatus(self):
        self.cells = [[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9,]]
        pass
 # end Game Definition

 # helper functions

    def BoardDraw(self):
        print("\n")
        print("\n")
        for row in self.cells:
            for element in row:
                print(element, end=" | ")
            print("")
            print("-"*12)

        pass

    def insertToken(self, token, num):

        for i, row in enumerate(self.cells):
            for j, element in enumerate(row):
                try:
                    if num == int(element):
                        self.cells[i][j] = token
                    else:
                        pass
                except:
                    pass

    def RowCheck(self, token):
        winner = [token, token, token]
        for row in self.cells:
            if row == winner:
                return True
            else:
                return False

    def Tie(self):
        for row in self.cells:
            for element in row:
                try:
                    if element in row and int(element):
                        return False
                except:
                    pass
        return True

    def ColumnCheck(self, token):
        winner = [token, token, token]
        col = []
        for i in range(0, 3):
            for row in self .cells:
                col.append(row[i])
                pass
            if col == winner:
                col = []
                return True
            else:
                col = []

    def DiagonalsCheck(self, token):
        winner = [token, token, token]
        diag1 = [row[i]for i, row in enumerate(self.cells)]
        diag2 = [row[-i-1] for i, row in enumerate(self.cells)]

        if diag1 == winner or diag2 == winner:
            return True
    # end helper functions

    def PlayGame(self):
        user1Choice = 0
        user2Choice = 0

        while True:

            while True:
                try:
                    player1 = int(input("Player 1 to play "))
                    if player1 >= 1 and player1 <= 9:
                        user1Choice = player1
                        break
                    else:
                        rprint(
                            "enter only valid number from 1 to 9 as the guide please")

                except:
                    rprint("enter only valid number from 1 to 9 as the guide please")
            self.insertToken(self.Token1, user1Choice)

            self.BoardDraw()

            while True:
                try:
                    player2 = int(input("Player 2 to play "))
                    if player2 >= 1 and player2 <= 9:
                        user2Choice = player2
                        break
                    else:
                        rprint(
                            "enter only valid number from 1 to 9 as the guide please")
                except:
                    print("enter only valid number from 1 to 9 as the guide please")
            self.insertToken(self.Token2, user2Choice)
            self.BoardDraw()

            if self.RowCheck(self.Token1) or self.ColumnCheck(self.Token1) or self.DiagonalsCheck(self.Token1):
                self.winStatus(1)
            elif self.RowCheck(self.Token2) or self.ColumnCheck(self.Token2) or self.DiagonalsCheck(self.Token2):
                self.winStatus(2)
            elif self.Tie():
                print("[blue]Its a Tie[/] "+"no one wins")
                self.resetStatus()
                break
