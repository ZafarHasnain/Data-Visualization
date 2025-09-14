#Shows trends over time or ordered data.
import matplotlib.pyplot as plt  

import numpy as np

x=[1,2,3,4,5,6,7,8,9,]
y1=[12,23,34,45,56,67,78,89,45]
y2=[90,89,78,67,56,45,46,23,44]

plt.plot(x,y1)
plt.plot(x,y2)
plt.show()