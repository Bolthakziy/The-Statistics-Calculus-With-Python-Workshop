import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt


gammaDistribution = np.random.gamma(1, size = 2000)
x = np.linspace(gammaDistribution.min(), gammaDistribution.max(), 2000)
y = stats.gamma.pdf(x, 1)

plt.hist(gammaDistribution, alpha = 0.3, bins = 25, density = True)
plt.plot(x, y)
plt.show()
