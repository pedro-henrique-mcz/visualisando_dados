'''Faendo o algoritmo de dados com matplotlib'''
import matplotlib.pyplot as plt
from die import Die

n = 1000
die = Die()

results = [die.roll() for _ in range(n)]
frequency = [results.count(value + 1) for value in range(die.num_sides)]

plt.style.use('_mpl-gallery')

x = [value + 1 for value in range(die.num_sides)]
y = frequency


fig, ax = plt.subplots()

ax.bar(x, y, width=1, edgecolor='white', linewidth=0.7)

ylim = max(results) + (max(results) * 1.1)

ax.set(xlim=(0,7), xticks=range(8),
       ylim=(0, ylim), yticks=[0,50,100,150,200])

plt.tight_layout()
plt.show()
