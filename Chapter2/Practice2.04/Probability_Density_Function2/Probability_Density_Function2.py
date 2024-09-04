import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


betaDistribution = np.random.beta(3, 7, size = 1500)
x = np.linspace(betaDistribution.min(), betaDistribution.max(), 1500)
y = stats.beta.pdf(x, 3, 7)

plt.hist(betaDistribution, alpha = 0.3, bins = 30, density = True)
plt.plot(x, y)
plt.show()
