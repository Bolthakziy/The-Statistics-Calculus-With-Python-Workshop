def calculate_factorial(number) :
	if number != 1 :
		return number * calculate_factorial(number - 1)
	else :
		return number

print("Let\'s learn the factorial calculation.")
num = int(input("Please enter a number. : "))
print("The factorial calculation is in progress.")
print("Now the calculation is done. The answer is below!")
print(calculate_factorial(num))
