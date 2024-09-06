import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


x = np.random.normal(2, 3, 2000)
y = np.random.normal(3, 1, 2000)

dataFrame = pd.DataFrame({"X_axis" : x, "Y_axis" : y})
dataFrame.head()

sns.jointplot(x = "X_axis", y = "Y_axis", data = dataFrame)
plt.show()
