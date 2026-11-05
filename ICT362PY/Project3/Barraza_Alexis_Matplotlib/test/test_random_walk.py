########################################################
# Software Req Doc: Project 3 Unit Testing             #
# Release Date: November 06, 2026                      #
# Coder: Alexis Barraza                                #
# Description: Unit testing for Random Walk.           #
########################################################

from Barraza_random_walk import RandomWalk


def test_random_walk_starts_at_origin():
    """REQ-RW-01: Test the random walk starts at (0,0)"""
    
    #Create a ranom walk
    rw = RandomWalk()
    # The first x,y-coordinate must be 0
    assert rw.x_values[0] == 0
    assert rw.y_values[0] == 0
    
    

def test_random_walk_number_of_points():
    """REQ-RW-02: Test that the walk creates the requested number of points."""
    
    #Create a random walk
    #The constructor in RandmWalk(num_points=5000)
    #I'm asking to get for only 100 points
    rw = RandomWalk(100)
    #Should fill in teh steps until both coordinates contain 100 points
    rw.fill_walk()
    
    #Assertions verify that only 100 points are allowed
    assert len(rw.x_values) == 100
    assert len(rw.y_values) == 100
    # This test should test the behavior of while len(self.x_values) < self.num_points
    

def test_random_walk_moves_each_step():
    """REQ-RW-03: Test that each step changes position."""
    
    #Create a random walk
    rw = RandomWalk(100)
    rw.fill_walk()
    
    
    for i in range(1, len(rw.x_values)):
        previous_point = (rw.x_values[i-1], rw.y_values[i-1])
        current_point = (rw.x_values[i], rw.y_values[i])
        
        assert current_point != previous_point