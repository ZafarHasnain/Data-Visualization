#Shows relationship between two numeric variables.
import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,8,9,10]
y=[2,3,5,7,45,23,12,33,44,6]
plt.scatter(x,y,label="stars", color="red",marker="*",s=30)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Scatter Plot")
plt.legend()
plt.show()