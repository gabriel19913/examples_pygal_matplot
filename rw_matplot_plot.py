from matplotlib import pyplot as plt
from random_walk import RandomWalk

# Creates a random walk and plot the points
while True:
    rw = RandomWalk()
    rw.fill_walk()

    # Defines the size of the window
    plt.figure(figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=10)
    # plt.plot(rw.x_values, rw.y_values, linewidth=1)

    # Emphasizes the first and the last points
    plt.scatter(0, 0, c='green', edgecolors='none', s=50)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=50)

    # Remove the axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    # Show the graph
    plt.show()

    # Loop to continuously generating the plots until the user stop it.
    option = input(('Make another walk? y/n '))
    if option == 'n':
        break
