'''
# Use the square number sequence 1, 4, 9, 16, 25 as the data for the graph.
import matplotlib.pyplot as plt
squares = [1, 4, 9, 16, 25]
plt.plot(squares)
plt.show()

import matplotlib.pyplot as plt
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)
# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)
plt.show()


# To plot a single point, use the scatter() function. Pass the single (x, y) values of the point of interest to scatter()
import matplotlib.pyplot as plt
plt.scatter(2, 4)
plt.show()


import matplotlib.pyplot as plt
plt.scatter(2, 4, s=200) # the size of the dots used to draw the graph
# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()


import matplotlib.pyplot as plt
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.scatter(x_values, y_values, s=100)
plt.show()

# y_values = [x**2 for x in x_values]  # squaring each number (x**2), and storing the results in y_values

Removing Outlines from Data Points
plt.scatter(x_values, y_values, edgecolor='none', s=40)

Defining Custom Colors
plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)

Defining colors using RGB
plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none', s=40)
'''

# Using a Colormap (looks like gradients)
'''A colormap is a series of colors in a gradient that moves from a starting to
ending color. Colormaps are used in visualizations to emphasize a pattern
in the data. For example, you might make low values a light color and high
values a darker color.

import matplotlib.pyplot as plt

x_values = list(range(1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
 edgecolor='none', s=40)
plt.show()
'''

'''
# Saving Your Plots Automatically
# If you want your program to automatically save the plot to a file, you can replace the call to plt.show() with a call to plt.savefig():

import matplotlib.pyplot as plt

x_values = list(range(1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
 edgecolor='none', s=40)
fname="test.png"
plt.savefig(fname)  # gonna be saved in the default path C:\Users\User\PycharmProjects\pythonProject\venv\Lib\site-packages\matplotlib\tests
'''

