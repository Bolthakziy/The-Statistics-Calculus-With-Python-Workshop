import pandas as pd
import numpy as np


myAnimalClass = {"CatClass" : [2, 100, 45, 32, 64, 39, 14], "RabbitClass" : [1, 4, 7, 27, 24, 36, 56]}
AnimalDataFrame = pd.DataFrame(myAnimalClass)
print("In first, this is my animal class!!!")
print()
print(AnimalDataFrame)
print()


AnimalDataFrame = AnimalDataFrame.rename(columns = {"CatClass" : "KatKlasse", "RabbitClass" : "KaninKlasse"})
print("Second, my animal class has a change. Its columns\' names are changed!!!")
print()
print(AnimalDataFrame)
print()


AnimalDataFrame = AnimalDataFrame.replace(to_replace = [32, 24], value =  0)
print("Third, some values in my animal class are modified.")
print()
print(AnimalDataFrame)
print()


myAnotherDataFrame = {"AndKlasse" : [1, 3, 5, 7, 9, 11, np.nan], "Koklasse" : [10, 20, 30, 40, 50, np.nan, 70]}
AnotherDataFrame = pd.DataFrame(myAnotherDataFrame)
AnimalDataFrame = pd.concat([AnimalDataFrame, AnotherDataFrame], axis = 1)
print("Forth, my animal class is remade.")
print()
print(AnimalDataFrame)
print()


AnimalDataFrame = AnimalDataFrame.fillna(121)
print("Fifth, \'NaN\' values will be gone.")
print()
print(AnimalDataFrame)
print()


AnimalDataFrame = AnimalDataFrame.drop([4, 6])
print("Sixth, Some Rows in my animal data frame are deleted.")
print()
print(AnimalDataFrame)
print()


NewDataFrame = pd.read_csv("./myCSVFile.csv")
print("Seventh, my new data frame!!!")
print()
print(NewDataFrame)
print()


print("Eighth, New data frame becomes ordered.")
print()
print(NewDataFrame.sort_values(by = "Hund"))
print(NewDataFrame.sort_values(by = "Kylling", ascending = False))
print(NewDataFrame)
print()


print("In last, you will get a \'CSV\' file.")
AnimalDataFrame.to_csv("./MyAnimalCSVFile.csv", sep = ',')
