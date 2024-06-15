x = int(input("Enter a number. : "))

if (x % 5 == 0) :
	if (x % 7 == 0) :
		print("x is divisible by 5 and 7.")
	elif (x % 9 == 0) :
		print("x is divisible by 5 and 9.")
	else :
		print("x is divisible by 5.")
elif (x % 7 == 0) :
	if (x % 9 == 0) :
		print("x is divisible by 7 and 9.")
	else :
		print("x is divisible by 7.")
elif (x % 9 == 0) :
	print("x is divisible by 9.")
else :
	print("x is not divisible by 5, 7 and 9.")
