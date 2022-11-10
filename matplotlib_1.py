import matplotlib.pyplot as plt
from random_walk import RandomWalk


# Make a random walk, and plot the points.
rw = RandomWalk(50000)
rw.fill_walk()

# Set the size of the plotting window.
plt.figure(figsize=(10, 6))


# Coloring the points
point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
 edgecolor='none', s=15)


plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
 edgecolor='none', s=1)

'''
# Plotting the Starting and Ending Points
plt.scatter(0, 0, c='green', edgecolors='none', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
 s=100)
'''

'''
# Remove the axes.
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
'''
plt.show()
