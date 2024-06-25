def is_It_Odd(number) :
	if (number & 1) == 0 :
		answer = False
	else :
		answer = True

	return answer

print("Let\'s play game!")
num = int(input("Enter thr number you think, please! : "))

if is_It_Odd(num) == False :
	print("Your number is a even number.")
else :
	print("Your number is an odd number.")
