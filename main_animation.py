from matplotlib.animation import FuncAnimation
from matplotlib.axes import Axes
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from is_prime import is_prime_number



x, y =[], []
_max = 1000
figSize = (6, 6)
prime = False
a,b = [], []
title = "Whole Number Cordinate"
if prime:
    for i in range(1, _max):
        if is_prime_number(i):
            a.append(i)
            b.append(i)
    title = "Prime Cordinate"
else:
    for i in range(1, _max):
        a.append(i)
        b.append(i)
a_it = iter(a)
b_it = iter(b)


def polarMapV2(figSize: tuple, prime: bool) -> tuple[Figure, Axes]: 
    fig, ax = plt.subplots(figsize=figSize, subplot_kw=dict(projection="polar"))
    return fig, ax

def update(frame):
    if len(a) != len(x) and len(b) != len(y): 
        x.append(next(a_it))
        y.append(next(b_it))
                
        ax.clear()
        ax.scatter(x, y, c="b", alpha=0.5)
        fig.canvas.draw()



fig, ax = polarMapV2(figSize, prime)
plt.title(title)
anim = FuncAnimation(fig, update, frames=1000, interval=30)
plt.show()
# anim.save("visualizer\src\Snapshots\whole.gif", writer="imagemagick")