from random import choice

class RandomWalk():
    ''''''
    def __init__(self, num_points=5000):
        ''''''
        self.num_points = num_points
        #nosso codigo
        self.x_values = [0]
        self.y_values = [0]
        self.xy_values = [(0,0)]

    def fill_walk(self):
        ''''''
        # Continua dando passos até que o passeio alcance o tamanho
        #desejado
        while len(self.x_values) < self.num_points:
                
            x_step = self.next_step()
            y_step = self.next_step()

            if x_step == 0 and y_step ==0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.xy_values.append((next_x, next_y))
            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def next_step(self):
        ''''''
        direction = choice([1, -1])
        distance = choice(list(range(5)))
        step = direction * distance

        return step
