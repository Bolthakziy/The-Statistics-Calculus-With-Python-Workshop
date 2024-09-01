import numpy as np
import matplotlib.pyplot as plt


firstAttribute = np.random.randn(100) * 3 + 2
secondAttribute = np.random.randn(100) *5 - 3

plt.hist(firstAttribute, color = 'g', bins = 70, alpha = 0.7)
plt.hist(secondAttribute, color = 'y', bins = 100, alpha = 0.2)
plt.show()
