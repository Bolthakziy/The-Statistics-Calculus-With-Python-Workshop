daysTuple = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

for i in range(12) :
	if i == 0 :
		print(f"{i + 1}st month has {daysTuple[i]} days.")
	elif i == 1 :
		print(f"{i + 1}nd month has {daysTuple[i]} days.")
	elif i == 2 :
		print(f"{i + 1}rd month has {daysTuple[i]} days.")
	else :
		print(f"{i + 1}th month has {daysTuple[i]} days.")
