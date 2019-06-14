import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def poincare_plot(data, DIMENSIONS=2):
    """
    Generate a poincare plot of the given time series.

    Parameters
    ----------
    data: list
        Time series data.
    DIMENSIONS: int, 2 or 3 if want visualized automatically.
        Number of embedding dimensions.

    Returns
    -------
    Embedded data.
    """

    out = [[] for i in range(DIMENSIONS)]

    for i in range(len(data) - DIMENSIONS + 1):
        for offset in range(DIMENSIONS):
            out[offset].append(data[i+offset])

    if DIMENSIONS in [2, 3]:
        fig = plt.figure()
        ax = Axes3D(fig) if DIMENSIONS == 3 else fig.add_subplot(111)

        ax.set_title("Poincare Plot")

        for i in range(DIMENSIONS):
            AXES = ['x', 'y', 'z']

            getattr(ax, f'set_{AXES[i]}label')(f'f(t{"+ " + str(i) if i else ""})')

        ax.scatter(*out)

        plt.show()

    return data


if __name__ == '__main__':
    data = np.random.uniform(size=100)

    poincare_plot(data)
