import pygal
from die import Die

# Create a D6.
die = Die()

# Make some rolls, and store results in a list.
results = []

for roll_num in range(1000):
    result = die.roll()     # a die we are usin is 6-side die (D6) to roll (1000 times). 1 to 6.
    results.append(result)

print(results)

print("\n")

# Analyze the results.
frequencies = []

for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')  # Save in my default python path as file:///C:/Users/User/PycharmProjects/pythonProject/die_visual.svg
