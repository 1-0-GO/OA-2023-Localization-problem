import matplotlib.pyplot as plt
import numpy as np
   

def naive_function(x, a, r):
    norm = np.linalg.norm(x - a, axis=-1)
    diff = norm - r
    diff_sq = diff **2
    summ = np.sum(diff_sq, axis=0)
    return summ

def relaxed_function(x, a, r):
    norm = np.linalg.norm(x - a, axis=-1)
    diff = norm - r
    diff_pos = np.where(diff<0, 0, diff)
    diff_sq = diff_pos **2
    summ = np.sum(diff_sq, axis=0)
    return summ


    

def plot_contour_2d(cost_function, anchors, ranges, delta, plot_dim_x, plot_dim_y, contour_plot, levels):
    def contour_plot1():
        fig, ax = plt.subplots()
        fig.set_size_inches(10, 6)
        xticks = np.linspace(*plot_dim_x, 10)
        yticks = np.linspace(*plot_dim_y, 9)
        ax.set_xticks(xticks)
        ax.set_yticks(yticks)
        label = 1
        for point in anchors:
            x_anchor, y_anchor = point
            ax.scatter(x_anchor, y_anchor, c='red', marker='o', s=100)
            ax.annotate('a' + str(label), (x_anchor, y_anchor), textcoords="offset points", xytext=(0, 10), ha='center')
            label += 1
        CS = ax.contour(X, Y, Z, levels=levels, cmap='terrain')
        ax.clabel(CS, inline=True, fontsize=10)    
    def contour_plot2():
        plt.figure(figsize=(8, 6))
        plt.contourf(X, Y, Z, levels=levels, cmap='viridis')
        plt.axis('scaled') 
        xticks = np.arange(*plot_dim_x, 0.5)
        yticks = np.arange(*plot_dim_y, 0.5)
        plt.xticks(xticks)
        plt.yticks(yticks)
        plt.colorbar()
        
    x = np.arange(*plot_dim_x, delta)
    y = np.arange(*plot_dim_y, delta)
    X, Y = np.meshgrid(x, y)
    grid_points = np.dstack((X, Y)).reshape(-1, 2)
    a_values = np.array(anchors)
    r_values = np.array(ranges)
    Z = cost_function(grid_points, a_values[:, np.newaxis, :], r_values[:, np.newaxis])
    Z = Z.reshape(X.shape)
    contour_plot1() if contour_plot == 1 else contour_plot2()
def task2():
    levels = np.concatenate(( np.array([0.025, 0.1]), np.arange(0.4, 11.2, 0.8) ))
    plot_contour_2d( naive_function, 
                         ( (-1, 0), (3, 0) ), 
                         (2, 3),
                         0.01, 
                         (-1.5, 3), (-3, 3),
                         1, levels)
    levels=15
    plot_contour_2d( naive_function, 
                         ( (-1, 0), (3, 0) ), 
                         (2, 3),
                         0.01, 
                         (-1.5, 2), (-2.5, 2.5),
                         2, levels) 
def task3():
    levels = np.arange(0, 6, 0.5)   
    plot_contour_2d( relaxed_function, 
                         ( (-1, 0), (3, 0) ), 
                         (2, 3),
                         0.01, 
                         (-1.5, 3), (-3, 3),
                         1, levels)
    levels=15
    plot_contour_2d( relaxed_function, 
                         ( (-1, 0), (3, 0) ), 
                         (2, 3),
                         0.01, 
                         (-1.5, 2.5), (-2.5, 2.5),
                         2, levels)
    