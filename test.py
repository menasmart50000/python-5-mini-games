
from string import *
from rich import print as rprint

mat = [[2, 4, 5, 7, 20],
       [3, 6, 8, 10, 18],
       [10, 12, 14, 16, 17],
       [20, 21, 22, 23, 24]]


# x = enumerate(mat)

# #  to get diagonals in matrix, use this algoritm
# # note, change offset will lead to get the next diagonal according
# # to column index
# offset = 3
# diag2 = [row[(-i-offset)] for i, row in x if 0 > (-i-offset) >= -len(row)]
# print(diag2)

# x = [[" "]*6 for row in range(7)]
# for row in x:
#     for element in row:
#         print(element, end="|")
#     print("")
#     print("-"*10)

wordlist = {}
mina = 'mina\n'
with open('wordle/wordlist.txt', mode="r") as wordGenerator:
    wordlist = wordGenerator.readlines()

for i, word in wordlist:
    wordlist[i] = word.strip('\n')

    print(wordlist)
