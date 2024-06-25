severalAnimals = {"Cat" : 4, "Bird" : 2, "Snake" : 0, "Ant" : 6, "Spider" : 8, "Squid" : 10, "Octopus" : 8}

def printLegs(animalName) :
	if severalAnimals[animalName] == 0 :
		print(f"The {animalName} does not have legs.")
	else :
		print(f"The {animalName} has {severalAnimals[animalName]} legs.")

while True :
	stillWantToKnow = input("Do you want to know how many legs an Animal has? : ")

	if (stillWantToKnow == 'Y') or (stillWantToKnow == 'y') :
		whichAnimal = str(input("Which animal do you want? : "))
		printLegs(whichAnimal)
	elif (stillWantToKnow == 'N') or (stillWantToKnow == 'n') :
		print("Goodbye!")
		break;
	else :
		print("Please enter the correct animal\'s name!")
