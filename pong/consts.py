"""
Constants for Pong

This module contains global constants for the game Pong. These constants are
accessed by other modules to accurately assign and use the given values. They are
used for assigning the paddle/ball's velocity and assigning the application's
width and height.

Author: Alvaro Deras
Date: December 30, 2023
"""

### WINDOW CONSTANTS (all coordinates are in pixels) ###

# the width of the game display
GAME_WIDTH = 1280
# the height of the game display
GAME_HEIGHT = 720

### PADDLE CONSTANTS ###

# the width of the paddle
PADDLE_WIDTH = 20
# the height of the paddle
PADDLE_HEIGHT = 100
# the number of pixels to move the paddle per update
PADDLE_MOVEMENT = 5

### BALL CONSTANTS ###

# the size of the ball
BALL_SIZE = 10
# the velocity of the ball
BALL_VELOCITY = 5
