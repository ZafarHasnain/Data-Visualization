#Displays distribution of a single numeric variable

import matplotlib.pyplot as plt
import numpy as np 


x= np.random.normal(160,13,256)


plt.hist(x)
plt.show( )