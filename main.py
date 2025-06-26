import pandas as pd
import numpy as np
import matplotlib as plt

# This is a test

# Pandas
df = pd.DataFrame({"A": [1, 2], "B": {3, 4}})
print(df)

# Numpy
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# Matplotlib
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()
