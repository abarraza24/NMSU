########################################################
# Software Req Doc: SRD Document UnitTesting           #
# Release Date: October 30, 2026                       #
# Coder: Alexis Barraza                                #
# Description: Unit Testing for Alein invasion game.   #
#               ship bullets                           #
########################################################

from alien_invasion import AlienInvasion


def test_bullet_limit():
    """The test should only fire three bullets or active bullets"""
    
    ai_game = AlienInvasion()
    #Fires 4 bullets
    ai_game._fire_bullet()
    ai_game._fire_bullet()
    ai_game._fire_bullet()
    ai_game._fire_bullet()
    
    
    assert len(ai_game.bullets) == 3
    
def test_bullet_moves_up():
    """Test that a bullet moves upward."""
    
    ai_game = AlienInvasion()
    
    
    #Fire one bullet
    ai_game._fire_bullet()
    #Than I grab that bullet using the index
    bullet = ai_game.bullets.sprites()[0]
    # Save its starting position
    starting_y = bullet.rect.y
    # Move the bullet upward
    bullet.update()
    # Bullet's new position should be smallere from where it started
    assert bullet.rect.y < starting_y
    
def test_ship_stays_inside_right_edge():
    """Test that the ship cannot move past the right edge."""

    ai_game = AlienInvasion()

    ai_game.ship.rect.right = ai_game.ship.screen_rect.right
    ai_game.ship.x = float(ai_game.ship.rect.x)

    ai_game.ship.moving_right = True
    ai_game.ship.update()

    assert ai_game.ship.rect.right <= ai_game.ship.screen_rect.right