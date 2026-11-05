########################################################
# Software Req Doc: Project 3 Unit Testing             #
# Release Date: November 06, 2026                      #
# Coder: Alexis Barraza                                #
# Description: Unit testing for Die class.             #
########################################################

from Barraza_Alexis_die import Die


def test_default_die_has_six_sides():
    """REQ-DICE-01: Test that a default die has six sides."""
    
    die = Die()
    
    assert die.num_sides == 6
    
    
def test_custom_die_has_ten_sides():
    """REQ-DICE-06: Test that custom die has ten sides"""
    die = Die(10)
    
    assert die.num_sides == 10
    
    
def test_die_roll_is_in_valid_range():
    """REQ-DICE-02: Test that die rolls stays within the valid range"""
    
    die = Die()
    
    for roll_num in range(100):
        result = die.roll()
        
        assert result >= 1
        assert result <= 6