########################################################
# Software Req Doc: SRD Document UnitTesting           #
# Release Date: October 30, 2026                       #
# Coder: Alexis Barraza                                #
# Description: Unit Testing for Alein invasion game.   #
#               Aliens                                 #
########################################################


from alien_invasion import AlienInvasion


def test_alien_fleet_created():
    """Test that the game creates an alien fleet."""
    
    ai_game = AlienInvasion()
    #Asking if there aliens
    assert len(ai_game.aliens) > 0
    

def test_alien_detects_screen_edge():
    """Tess that an alien detects the right edge."""
    
    ai_game = AlienInvasion()
    
    alien = ai_game.aliens.sprites()[0]
    
    alien.rect.right = ai_game.screen.get_rect().right
    
    assert alien.check_edges()
    
def test_fleet_changes_directions():
    """Test the fleet drops and changes directions."""
    
    ai_game = AlienInvasion()
    
    alien = ai_game.aliens.sprites()[0]
    # We need to save aliens moving righ
    starting_y = alien.rect.y
    # We save aliens moving down and left
    starting_directions = ai_game.settings.fleet_direction
    
    ai_game._change_fleet_direction()
    
    assert ai_game.settings.fleet_direction == starting_directions * -1
    assert alien.rect.y == starting_y + ai_game.settings.fleet_drop_speed