import matplotlib.pyplot as plt
import numpy as np


firstType = [1, 1]
secondType = [2, 2]
thirdType = [1, 4]

Types = [firstType, secondType, thirdType]
position = np.array([0, 1, 2])

belowBar = plt.bar(position, [Type[0] for Type in Types])
aboveBar = plt.bar(position, [Type[1] for Type in Types], bottom = [Type[0] for Type in Types])

plt.xticks(position, ['A', 'B', 'C'])
plt.legend([belowBar, aboveBar], ["Down", "Up"])
plt.show()
