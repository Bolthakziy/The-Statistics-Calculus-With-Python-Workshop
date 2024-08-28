import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(1, 10, 2000)

linearLine = x * 3
logLine = np.log(x)
tangentLine = np.sin(x)

lines = [linearLine, logLine, tangentLine]
colors = ['r', 'g', 'b']
styles = ['-', ':', 'solid']


for line, color, style in zip(lines, colors, styles) :
	plt.plot(x, line, c=color, linestyle=style)


plt.show()
