import numpy as np
from timeit import Timer
import math

myList = list(range(0, 1000))
myArray = np.array(myList)
print("myList")
print(myList)
print()
print("myArray")
print(myArray)
print()


def add_ThreeForElementsInList() :
	for element in myList :
		element += 3

	return myList

def add_ThreeForElementsInArray() :
	return (myArray + 3)


print("Computing time for \'add_ThreeForElementsInList\' is below.")
print(min(Timer(add_ThreeForElementsInList).repeat(10, 10)))
print()
print("Computing time for \'add_ThreeForElementsInArray\' is below.")
print(min(Timer(add_ThreeForElementsInArray).repeat(10, 10)))
print()


def multiply_FiveForElementsInList() :
	for element in myList :
		element *= 5

	return myList

def multiply_FiveForElementsInArray() :
	return (myArray * 5)



print("Computing time for \'multiply_FiveForElementsInList\' is below.")
print(min(Timer(multiply_FiveForElementsInList).repeat(10, 10)))
print()
print("Computing time for \'multiply_FiveForElementsInArray\' is below.")
print(min(Timer(multiply_FiveForElementsInArray).repeat(10, 10)))
print()


myList2 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]
myArray2 = np.array(myList2)


def square_ElementsInList() :
	for element in myList2 :
		math.sqrt(element)

	return myList2

def square_ElementsInArray() :
	return (np.sqrt(myArray2))



print("Computing time for \'square_ElementsInList\' is below.")
print(min(Timer(square_ElementsInList).repeat(10, 10)))
print()
print("Computing time for \'square_ElementsInArray\' is below.")
print(min(Timer(square_ElementsInArray).repeat(10, 10)))
print()
