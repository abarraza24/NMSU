########################################################
# Software Req Doc: Project 3 Unit Testing             #
# Release Date: November 06, 2026                      #
# Coder: Alexis Barraza                                #
# Description: Unit testing for Matplotlib data.       #
########################################################

from Barraza_Alexis_mpl_squares import square_data


def test_square_input_values():
    """REQ-MPL-01: Test that the correct input values are generated."""
    
    input_values, squares = square_data()
    
    assert input_values == [1, 2, 3, 4, 5]
    

def test_square_output_values():
    """REQ-MPL-02: Test that the correct square values are generated."""

    input_values, squares = square_data()

    assert squares == [1, 4, 9, 16, 25]
    
def test_values_are_squares():
    """REQ-MPL-02: Test that each output is the square of its input."""

    input_values, squares = square_data()

    for i in range(len(input_values)):
        assert squares[i] == input_values[i] ** 2