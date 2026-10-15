import numpy as np
import matplotlib.pyplot as plt
def display_curves():
    x = np.linspace(-10, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = x ** 2
    y4 = np.exp(x / 5)
    plt.plot(x, y1, label="Sine")
    plt.plot(x, y2, label="Cosine")
    plt.plot(x, y3, label="Polynomial")
    plt.plot(x, y4, label="Exponential")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Sine, Cosine, Polynomial and Exponential Curves")
    plt.legend()
    plt.grid()
    plt.show()
display_curves()