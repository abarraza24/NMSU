########################################################
# Software Req Doc: Data Analysis                      #
# Release Date: November 06, 2026                      #
# Coder: Alexis Barraza                                #
# Description: Random Walk Class visual                   #
########################################################
import matplotlib.pyplot as plt

from Barraza_random_walk import RandomWalk

# Keep making new walks
while True:
    # Make a random walk.
    rw = RandomWalk(50_000)
    rw.fill_walk()
    
    
    #Plot the point to walk
    plt.style.use('classic')
    fig, ax= plt.subplots()
    
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
    
    #Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    plt.show()
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break