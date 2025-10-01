import pygal

from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()


xy_chart = pygal.XY(stroke=False)
xy_chart.add(
    'start',
    [rw.xy_values[0]],
    dots_size = 5
)

xy_chart.add(
    'steps',
    [*rw.xy_values],
    dots_size = 1
)

xy_chart.add(
    'end',
    [rw.xy_values[rw.num_points - 1]],
    dots_size= 5
)


xy_chart.render_to_file('rw_file.svg')


# xy_chart.add(
#     'y = cos(x)',
#     [(cos(x / 10.), x / 10.) for x in range(-50, 50, 5)],
#     color='red',         # Define a cor da linha e dos pontos
#     dots_size=5,         # Define o tamanho dos pontos
#     stroke_width=3       # Define a espessura da linha
# )