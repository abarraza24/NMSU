########################################################
# Software Req Doc: SRD Document UnitTesting           #
# Release Date: October 30, 2026                       #
# Coder: Alexis Barraza                                #
# Description: Unit Testing for Alein invasion game.   #
#               Scoring                                #
########################################################

from alien_invasion import AlienInvasion
from alien import Alien

def test_play_button_resets_game():
    """Test the Play button resets the game stats"""
    
    ai_game = AlienInvasion()
    
    ai_game.stats.score = 500
    ai_game.stats.level = 3
    ai_game.stats.ships_left = 1
    
    #Pretending a player clicks the Play button
    mouse_pos = ai_game.play_button.rect.center
    # Then center of the buttom is inside the button
    ai_game._check_play_button(mouse_pos)
    #That should reset everything
    assert ai_game.stats.score == 0
    assert ai_game.stats.level == 1
    assert ai_game.stats.ships_left == ai_game.settings.ship_limit
    assert ai_game.game_active
    
    
def test_score_increase_when_alien_hit():
    """Test destroying an alien increases the score."""
    
    ai_game = AlienInvasion()
    
    ai_game.aliens.empty()
    ai_game.bullets.empty()
    
    ai_game._fire_bullet()
    bullet = ai_game.bullets.sprites()[0]
    
    alien = Alien(ai_game)
    alien.rect.center = bullet.rect.center
    ai_game.aliens.add(alien)
    
    alien_points = ai_game.settings.alien_points
    
    ai_game._check_bullet_alien_collisions()
    
    assert ai_game.stats.score == alien_points
    

def test_level_and_speed_increase():
    """Test clearing a fleet increases the difficulty and game speed"""
    
    ai_game = AlienInvasion()
    
    starting_level = ai_game.stats.level
    starting_alien_speed = ai_game.settings.alien_speed
    
    ai_game.aliens.empty()
    
    ai_game._check_bullet_alien_collisions()
    
    assert ai_game.stats.level == starting_level + 1
    assert ai_game.settings.alien_speed > starting_alien_speed