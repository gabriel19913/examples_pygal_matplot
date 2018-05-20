from random_walk import RandomWalk
import pygal
from pygal.style import CleanStyle

# Creates a random walk
rw = RandomWalk()
rw.fill_walk()

# Creates a chart to show the points
chart = pygal.XY(stroke=False, style=CleanStyle, show_legend=False, human_readable=True, fill=False, show_dots=True, dot_size=4, show_x_labels=False, show_y_labels=False)

chart.title = 'Random Walk Pygal'
coordi_x = []
coordi_y = []
coordinates = []

# The x coordinates are generated
for x in rw.x_values:
    coordi_x.append(x)
# The y coordinates are generated
for y in rw.y_values:
    coordi_y.append(y)
# The list of coordinates are generated
for i in range(rw.num_points):
    aux = (coordi_x[i], coordi_y[i])
    coordinates.append(aux)
chart.add('P', coordinates)
# Save the graph in a svg file
chart.render_to_file('random_walk_pygal.svg')
