import pandas as pd


def discriminate_Number(number) :
	if (number % 2 == 0) :
		return "even"
	else :
		return "odd"


myDataFrame = pd.DataFrame({ "x" : [3, 5, 9], "y" : [-6, 8, 2], "z" : [-7, 1, -9]})
print("First data frame.")
print()
print(myDataFrame)
print()


myDataFrame["xPlus7"] = myDataFrame["x"].apply(lambda x : x + 7)
print("Second data frame.")
print()
print(myDataFrame)
print()


myDataFrame["WhatIsY"] = myDataFrame["y"].apply(discriminate_Number)
print("Third data frame")
print()
print(myDataFrame)
print()


print("Applying one-hot encoding to \'WhatISY\' column.")
print()
print(pd.get_dummies(myDataFrame["WhatIsY"]))
print()


print("Check data distributions.")
print()
print(myDataFrame["WhatIsY"].value_counts())
