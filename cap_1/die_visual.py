from die import Die
import pygal

die_1 = Die(6)
die_2 = Die(6)

results = []
n = 1000

results = [die_1.roll() * die_2.roll()  for _ in range(n)]

frequencies = []
max_result = die_1.num_sides + die_2.num_sides 

frequencies = [results.count(value) for value in range(2, max_result+1)]

hist = pygal.Bar()

hist.title = f"{n} times"
hist.x_labels = [str(value) for value in range(max_result+1)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6' + 'D6', frequencies)
hist.render_to_file('dice.svg')
