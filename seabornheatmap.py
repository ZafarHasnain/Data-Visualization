#Shows data density or correlation in matrix form.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
df=np.random.rand(12,13)
# print(df)

sns.heatmap(df)
plt.show()


