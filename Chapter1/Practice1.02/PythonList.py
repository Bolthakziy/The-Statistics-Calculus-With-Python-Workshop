myList = [1650, 'Y', (4, 7), 38]
print(myList)

print("First Printing : myList[2]")
print(myList[2])
print("Second Printing : myList[1 : 3]")
print(myList[1 : 3])

myList.append(17)
print("Third Printing : second myList")
print(myList)
anotherMyList = [1, 4, 9, 16, 25]
print("Forth Printing : myList + anotherMyList")
print(myList + anotherMyList)

for i in range(4) :
	myList.pop()
print("Fifth Printing : third myList")
print(myList)
myList = myList + anotherMyList
print("Sixth Printing : forth myList")
print(myList)

otherList = [3 * factor for factor in myList if factor % 2 == 1]
print("Seventh printing : otherList")
print(otherList)
