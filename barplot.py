#Compares categorical data.
import matplotlib.pyplot as plt
import numpy as np

x=["lahore","Karachi","Islamabad","Mianwali","bakhar","kotadu"]
y=[123,345,234,234,456,876,]
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title=('Bar plot')
plt.bar(x,y,color='green',edgecolor='yellow',)
plt.show()