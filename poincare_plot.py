import numpy as np
import matplotlib.pyplot as plt


def poincare_plot(data):
    X = []
    Y = []

    for i in range(len(data) - 1):
        X.append(data[i])
        Y.append(data[i+1])

    plt.title("Poincare Plot")
    plt.scatter(X, Y)
    plt.show()

    return X, Y
