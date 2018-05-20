from die import Die
import pygal

die = Die()
results = []
# Rolls the dice 1000 times
for number in range(1000):
    results.append(die.roll())
frequencies = []
# Counts the frequence of appearance of each dice number
for value in range(1, die.num_sides + 1):
    frequencies.append(results.count(value))
print(frequencies)
# Generates a bar graph with the frequency of each number
hist = pygal.Bar()
hist.title = 'Results of rowling a D6 1000 times'
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = 'Result'
hist.y_title = 'Frequency of result'

hist.add('D6', frequencies)
# Save the graph in a svg file
hist.render_to_file('die_visual.svg')
