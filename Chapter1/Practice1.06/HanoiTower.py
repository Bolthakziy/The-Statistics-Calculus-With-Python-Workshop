def Hanoi_print(src, dest) :
	print(f"A disc is carried from {src} to {dest}")

def Hanoi_carry(discNumber, startPosition, middlePosition, targetPosition) :
	if discNumber == 1 :
		Hanoi_print(startPosition, targetPosition)
	elif discNumber < 1 :
		print("Please enter a correct disc number....")
	else :
		Hanoi_carry(discNumber - 1, startPosition, targetPosition, middlePosition)
		Hanoi_print(startPosition, targetPosition)
		Hanoi_carry(discNumber - 1, middlePosition, startPosition, targetPosition)

def MovingCount_get(discNumber) :
	if discNumber == 1 :
		return 1
	elif discNumber < 1 :
		print("Please enter a correct disc number....")
	else :
		return 2 * MovingCount_get(discNumber - 1) + 1
