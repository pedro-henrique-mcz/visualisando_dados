import matplotlib.pyplot as plt
import pygal 
from rand_walk import RandomWalk
from die import Die
import numpy as np


def show_walk_matplotlib():
    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use('_mpl-gallery')

    x = rw.x_values
    y = rw.y_values

    fig, ax = plt.subplots(figsize=(10,6))

    point_numbers = list(range(rw.num_points))
    ax.scatter(x, y, s=4, c=point_numbers, cmap=plt.cm.Blues)

    ax.scatter(0,0, c='red', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.tight_layout()

    plt.show()

def show_dices_matplotlib():
    plt.style.use('_mpl-gallery')
    die = Die()

    x = die.mult_roll(1000)
    bins = np.arange(0.5, 7.5, 1)

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.hist(x, bins=bins, edgecolor='white')
    ax.set(xlim=(-0.5, 7.5), xticks=range(-1,8))


    plt.tight_layout()
    plt.show()

def show_die_pygol():
    die = Die()

    results = die.mult_roll(1000)

    frequency = [results.count(value) for value in range(1, die.num_sides + 1)]

    hist = pygal.Bar()

    hist.title= 'Relembrando dados'
    hist.x_labels = [str(value) for value in range(1, die.num_sides + 1)]
    hist.x_title = 'Valores'
    hist.y_title = 'Resultados'

    hist.add('D6', frequency)
    hist.render_to_file('dice.svg')


rw = RandomWalk()
rw.fill_walk()

xy_chart = pygal.XY(stroke=False)
xy_chart.title = 'Pygal Random Walk'

xy_chart.add(
    'Start', 
    [rw.xy_values[0]],
    dots_size=5
)
xy_chart.add(
    'Steps', 
    rw.xy_values,
    dots_size='1'
)
xy_chart.add(
    'End', 
    [rw.xy_values[len(rw.xy_values) -1]],
    dots_size='5'
)

xy_chart.render_to_file('rw_file.svg')
