import pandas as pd

myDictionary = {'col1' : [10, 20, 30], 'col2' :  [35, 45, 55], 'col3' : [97, 98, 99]}
myDataFrame = pd.DataFrame(myDictionary)


print("This is my dictionary.")
print()
print(myDataFrame)
print()


print("Row 0 ~ Row 1 in my dictionary.")
print()
print(myDataFrame.loc[[0, 1]])
print()


print("Column 1, Column 3 in Row 1 in my dictionary.")
print()
print(myDataFrame.loc[1, ['col1', 'col3']])
print()


print("Column 2 in my dictionary.")
print()
print(myDataFrame['col2'])
print()


print("Column 1 in my dictionary.")
print()
for i in myDataFrame.loc[ :, 'col1'] :
	print(i)
print()


myDataFrame.loc[0] = [1, 4, 9]
print("This is first change in my dictionary.")
print()
print(myDataFrame)
print()


myDataFrame['col3'] = [16, 25, 36]
print("This is second change in my dictionary.")
print()
print(myDataFrame)
print()


print("Row 1 with Column 0, Column 1 in my dictionary.")
print(myDataFrame.loc[[False, True, False], [True, True, False]])
print()


print("The values except in Column 1 will be printed.")
print(myDataFrame.loc[:, myDataFrame.loc[2] > 30])
