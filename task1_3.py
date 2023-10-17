import matplotlib.pyplot as plt
import numpy as np


def non_convex_function(x, a, r):
    norm = np.abs(x-a)
    diff = norm - r
    diff_sq = diff **2
    summ = np.sum(diff_sq, axis=0)
    return summ

def convex_function(x, a, r):
    norm = np.abs(x-a)
    diff = norm - r
    diff_pos = np.where(diff<0, 0, diff)
    diff_sq = diff_pos **2
    summ = np.sum(diff_sq, axis=0)
    return summ

def plot_1d(cost_function, anchors, r, delta, plot_dim_x):
    x = np.arange(*plot_dim_x, delta)
    anchors = np.array(anchors)
    a_values = anchors[:, np.newaxis]
    r = np.array(r)
    r_values = r[:, np.newaxis]
    y = cost_function(x, a_values, r_values)
    plt.plot(x, y)
    plt.show()

plot_1d(non_convex_function, (2,), (1,), 0.01, (-1,5))
plot_1d(convex_function, (2,), (1,), 0.01, (-1,5))