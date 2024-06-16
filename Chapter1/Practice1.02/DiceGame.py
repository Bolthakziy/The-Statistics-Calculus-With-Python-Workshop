import random

dice_value = random.randint(0, 7)

while True :
	guess = int(input("Enter your dice number. : "))

	if (guess == dice_value) :
		print("You find the exact dice number. Very good.")
		break;
	elif (guess > dice_value) :
		print("Your answer is bigger than the dice value....")
	else :
		print("Your answer is lower than the dice value....")
