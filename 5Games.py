from gtn import GuessTheNumber
from rps import RPS
from wordle import wordle
from C4 import Connect4
from TTT import TicTacToe
while True:
    user = input("""
    The Games:
    - Guess The Number Python(1)
    - Rock Paper Scissors Python(2)
    - Wordle Python(3)
    - Connect Four Python(4)
    - Tic Tac Toe Python(5)
    -Quit(q)
    """)
    if user == "1":
        GuessTheNumber(50)
    elif user == "2":
        RPS()
    elif user == "3":
        word = wordle()
        word.playGame()
    elif user == "4":
        C4 = Connect4()
        C4.PlayGame()
    elif user == "1":
        pass
    elif user == "5":
        TiTaTc = TicTacToe()
        TiTaTc.PlayGame()
    elif user == "q":
        confirm = input("Are you sure? YES:y, NO:n")
        if confirm == "y":
            print("Thank you sure!")
            break
        elif confirm == "n":
            pass
