########################################################
# Software Req Doc: Data Analysis                      #
# Release Date: November 06, 2026                      #
# Coder: Alexis Barraza                                #
# Description: Die                                      #
########################################################

from random import randint


class Die:
    """A class representing a singel die"""
    
    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.num_sides = num_sides
        
    def roll(self):
        """Returns a random value between 1 and number of sides"""
        return randint(1, self.num_sides)