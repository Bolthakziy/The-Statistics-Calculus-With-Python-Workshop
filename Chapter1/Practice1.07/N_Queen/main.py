from N_Queens import *

boardSize = int(input("Enter the size of your chess board. : "))
chessBoard = []

for i in range(boardSize) :
	chessBoard.append([])
	for j in range(boardSize) :
		chessBoard[i].append(0)

finalBoard = find_Solution(chessBoard, 0, boardSize)

if finalBoard is False :
	print("There is no board for the solution....")
else :
	print("There is the below board for the solution!")
	print_chessBoard(chessBoard, boardSize)
