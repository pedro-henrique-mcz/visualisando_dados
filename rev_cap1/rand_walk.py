from random import choice

class RandomWalk():
    ''''''
    def __init__(self, num_points=5000, distance=5):
        ''''''
        self.num_points = num_points
        self.distance = distance

        self.x_values = [0]
        self.y_values = [0]

        self.xy_values =[(self.x_values[0], self.y_values[0])]

    def fill_walk(self):
        ''''''
        while len(self.x_values) < self.num_points:

            x = self.next_step() 
            y = self.next_step()  

            if x == 0 and y == 0: 
                pass

            next_x = x + self.x_values[-1]
            next_y = y + self.y_values[-1]

            self.x_values.append(next_x)
            self.y_values.append(next_y)
            self.xy_values.append((next_x, next_y))
    
    def next_step(self):
        ''''''
        direction = choice([1,-1])
        distance = choice(list(range(self.distance)))
        return direction * distance
