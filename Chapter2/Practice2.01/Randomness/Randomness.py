import numpy as np

print("A set with elements between 10 and 50.")
firstArray = np.random.randint(low=10, high=50, size=(7, 7))
print(firstArray)
print()
print()
print("Some lists from the list \'[1, 3, 5, 7, 9]\'.")
secondArray = np.random.choice([1, 3, 5, 7, 9], size=(3, 3))
print(secondArray)
print()
print()
myList = [2, 4, 6, 8]
print("Shuffle works with the list \'[2, 4, 6, 8]\'.")
for i in range(0, 5) :
	np.random.shuffle(myList)
	print(myList)
