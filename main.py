from matplotlib.axes import Axes
import matplotlib.pyplot as plt
from is_prime import is_prime_number


def polarMap(figSize: tuple, prime: bool) -> Axes:
    plt.figure(figsize=figSize)
    title = "Whole Number Cordinate"
    if prime:
        title = "Prime Cordinate"
    ax = plt.subplot(polar=True)
    plt.title(title)
    return ax


def polarPlotter(ax: Axes, max: int, prime: bool):
    if prime:
        for i in range(1, max):
            if is_prime_number(i):
                ax.scatter(i, i)
    else:
        for i in range(1, max):
            ax.scatter(i, i)


if __name__ =="__main__":
    max = 1000
    figSize = (6, 6)
    prime = True

    ax = polarMap(figSize, prime)
    polarPlotter(ax, max, prime)
    plt.show()