from random import choice


class RandomWalk():
    '''A class that enerates a random walk'''
    def __init__(self, num_points=5000):
        self.num_points = num_points
        # The walks start in the coordinate 0,0
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        '''Calculates the step'''
        # Chose the walk direction
        direction = choice([1, -1])
        # Chose the walk distance in the axis
        distance = choice([0, 1, 2, 3, 4])
        # Calculates the step in the chosen direction
        step = direction * distance
        return step

    def fill_walk(self):
        # Continues until to reach the desired number of points
        while len(self.y_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()
            # Calculates the next step
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)
