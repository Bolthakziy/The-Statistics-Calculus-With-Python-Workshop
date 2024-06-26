def get_min(numberList) :
	minIndex = 0

	for idx, content in enumerate(numberList) :
		if content < numberList[minIndex] :
			minIndex = idx

	return minIndex, numberList[minIndex]

print("Please enter till 10 numbers!")
print("Let\'s find the minimum number!")
myList = []

for i in range(0, 10) :
	num = int(input("Enter your number till 10. : "))
	myList.append(num)

print("Entering works are done.")
print("We find that the minimum number.")
print("In a below tuple, first number is the index of the minimum number.")
print("And second number is the minimum number.")
print(get_min(myList))
