MultidimensionList = [[1, 2, 3], [1, 4, 9], [1, 8, 27]]

print("First printing.")
for row in MultidimensionList :
	print(row[1])

print("Second printing.")
for row in MultidimensionList :
	print(row)

print("Third printing.")
for row in MultidimensionList :
	for element in row :
		print(element)

print("Forth printing.")
for i in range(3) :
	if i == 0 :
		print(f"The {i + 1}st diagonal element : {MultidimensionList[i][i]}")
	elif i == 1 :
		print(f"The {i + 1}nd diagonal element : {MultidimensionList[i][i]}")
	else :
		print(f"The {i + 1}rd diagonal element : {MultidimensionList[i][i]}")
