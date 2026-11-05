########################################################
# Software Req Doc: Data Analysis                      #
# Release Date: November 06, 2026                      #
# Coder: Alexis Barraza                                #
# Description: Plotting_simple_line_graph              #
########################################################
import matplotlib.pyplot as plt

#Wanted to seprate methods
# Since I could not figure out how to test visuals
# This helps me without opening a chart
def square_data():
    """Return the input values and thier square values."""
    
    input_values = [1,2,3,4,5]
    squares = [1,4,9,16,25]
    
    return input_values, squares


def main():
    """Create and display the square number line graph."""
    
    input_values, squares = square_data()
    
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    ax.plot(input_values, squares, linewidth=3)
    
    #Set chart title and label axes
    ax.set_title("Square Numbers", fontsize=24)
    ax.set_xlabel("Value", fontsize=14)
    ax.set_ylabel("Square of Value", fontsize=14)
    
    #Set ssize of tick labels.
    ax.tick_params(axis='both', labelsize=14)
    plt.show()
    
    
if __name__ == "__main__":
    main()