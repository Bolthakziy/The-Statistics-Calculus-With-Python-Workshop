import pandas as pd


StudentsSet = pd.DataFrame({"name" : ["Alexander", "Laura", "Daniel", "Peter", "Constantine", "Isabel"], \
			    "gender" : ["male", "female", "male", "male", "male", "female"], \
			    "class" : ["1st", "1st", "3rd", "2nd", "1st", "4th"], \
			    "sum" : [80, 75, 74, 86, 72, 96], \
			    "number" : [4, 3, 2, 2, 6, 3]})
print("1st Students Data.")
print()
print(StudentsSet)
print()


StudentsSet["IsFemale?"] = StudentsSet["gender"].apply(lambda g : g == "female")
StudentsSet = StudentsSet.drop("gender", axis = 1)
print("2nd Students Data.")
print()
print(StudentsSet)
print()


StudentsSet = pd.concat([StudentsSet.drop("class", axis = 1), pd.get_dummies(StudentsSet["class"])], axis = 1)
print("3rd Students Data.")
print()
print(StudentsSet)
print()


print("We will know the average of the girls\' sum and the boys\' sum.")
girlGroup = StudentsSet.groupby("IsFemale?")
print(girlGroup["sum"].mean())
print()


print("Now we will know the number of the girls\' subjects and the boys\' subjects.")
print(girlGroup["number"].sum())
