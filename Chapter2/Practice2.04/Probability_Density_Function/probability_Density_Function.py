import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


normalDistribution = np.random.normal(0, 1, size = 3000)

x = np.linspace(normalDistribution.min(), normalDistribution.max(), 3000)
y = stats.norm.pdf(x)

plt.hist(normalDistribution, alpha = 0.3, bins = 30, density = True)
plt.plot(x, y)
plt.show()
