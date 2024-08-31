import matplotlib.pyplot as plt
import numpy as np


firstType = [3, 3]
secondType = [4, 2]
thirdType = [1, 5]

Types = [firstType, secondType, thirdType]

position = np.array([0, 1, 2])
barWidth = 0.3

leftBar = plt.bar(position - barWidth / 2, [Type[0] for Type in Types], width = barWidth)
rightBar = plt.bar(position + barWidth / 2, [Type[1] for Type in Types], width = barWidth)

plt.xticks(position, ['A', 'B', 'C'])
plt.legend([leftBar, rightBar], ["Left", "Right"])
plt.show()
