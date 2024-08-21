import pandas as pd
import numpy as np


myDataTable = pd.read_csv("dataTable.csv", index_col = "ID")
print("My data table from a \'CSV\' file.")
print()
print(myDataTable)
print()


myDataTable = myDataTable.rename(columns = {"X" : "DT_X", "Y" : "DT_Y", "Z" : "DT_Z"})
print("The columns of my data table are changed.")
print()
print(myDataTable)
print()


myDataTable = myDataTable.drop(4, axis = 0)
print("A row in my data table is gone.")
print()
print(myDataTable)
print()


newTable = pd.DataFrame(np.zeros((2, 3)), columns = ["DT_X", "DT_Y", "DT_Z"])
myDataTable = pd.concat([myDataTable, newTable], axis = 0)
print("My data table has new more values.")
print()
print(myDataTable)
print()


myDataTable = myDataTable.sort_values("DT_Y", axis = 0)
print("A some part in my data table is ordered.")
print()
print(myDataTable)
print()


myDataTable = myDataTable.astype(int)
myDataTable.to_csv("NewDataTable.csv", index = False)
print("In last, you will get a new \'CSV\' file!!!")
