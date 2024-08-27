import matplotlib.pyplot as plt


x = [1, 2, 3]
y = [4, 5, 6]
size = [30, 100, 70]
color = ['r', 'b', 'g']

plt.scatter(x, y, s=size, c=color)
plt.show()
