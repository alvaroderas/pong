"""
Models module for Pong

This module contains the model classes for the Pong game. This includes classes
for the buttons, paddles, and ball.

Author: Alvaro Deras
Date: December 30, 2023
"""
from consts import *
import pygame, sys

class Button():
    """
    The Button class represents a button in the Pong game. It is used for
    creating interactive buttons with different colors for normal and hovering
    states depending on the user's cursor.
    """
	def __init__(self, pos, text_input, font, base_color, hovering_color):
        """
        Initializes a Button object with specified position, text input, font,
        base color, and hovering color.

        Parameter pos: the position of the button
        Precondition: pos is a tuple or list with two numerical values

        Parameter text_input: the button's text
        Precondition: text_input is a String

        Parameter font: the font of the text
        Precondition: font is a Pygame font object

        Parameter base_color: the base color of the text
        Precondition: base_color is a String representing a valid color

        Parameter hovering_color: the color when hovering over the text
        Precondition: hovering_color is a String representing a valid color
        """
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)

		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
        """
        Updates the button on the given screen.

        Parameter screen: the screen of the application
        Precondition: screen is a Pygame surface object
        """
		screen.blit(self.text, self.text_rect)

	def check_input(self, position):
        """
        Returns whether the given position is within the bounds of the button.

        Parameter position: the x, y coordinates of the mouse
        Precondition: position is a tuple or list containing two numerical values
        """
		if position[0] in range(self.text_rect.left, self.text_rect.right) and position[1] in range(self.text_rect.top, self.text_rect.bottom):
			return True
		return False

	def change_color(self, position):
        """
        Changes the button color based on the mouse position.

        Parameter position: the x, y coordinates of the mouse
        Precondition: position is a tuple or list containing two numerical values
        """
		if position[0] in range(self.text_rect.left, self.text_rect.right) and position[1] in range(self.text_rect.top, self.text_rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)


class Player(pygame.sprite.Sprite):
    """
    The Player class represents a player in the Pong game. It defines the left
    and right paddles for the players.
    """
    def __init__(self):
        super(Player, self).__init__()
        self.left_paddle = pygame.Surface((20, 100))
        self.left_paddle.fill((255, 255, 255))
        self.left_rect = self.left_paddle.get_rect(topleft = (30, 310))
        self.right_paddle = pygame.Surface((20, 100))
        self.right_paddle.fill((255, 255, 255))
        self.right_rect = self.right_paddle.get_rect(topleft = (1230, 310))

player = Player()

class Ball():
    """
    The Ball class represents the ball in the Pong game. It manages the ball's
    position, movement, collision, and resetting.
    """

    def __init__(self):
        """
        Initializes a Ball object with default starting coordinates and
        velocities.
        """
        self.x = 637
        self.y = 350

        self.velocity_y = 0
        self.velocity_x = BALL_VELOCITY
        self.velocity = BALL_VELOCITY

    def draw(self, screen):
        """
        Draws the ball on the given screen.

        Parameter screen: the screen of the application
        Precondition: screen is a Pygame surface object
        """
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), 10)

    def move(self):
        """
        Moves the ball based on its velocity.
        """
        self.y += self.velocity_y
        self.x += self.velocity_x

    def collision(self, screen):
        """
        Handles ball collision with paddles and screen boundaries.

        Parameter screen: the screen of the application
        Precondition: screen is a Pygame surface object
        """
        if self.y >= 710:
            self.velocity_y = -1 * self.velocity_y
        if self.y - 5 <= 0:
            self.velocity_y = -1 * self.velocity_y

        if self.velocity_x < 0:
            if self.y >= player.left_rect.y and self.y <= player.left_rect.y + 100:
                if self.x <= player.left_rect.x + 20:
                    self.velocity_x = self.velocity_x * -1
                    middle_y = player.left_rect.y + 50
                    difference_in_y = middle_y - self.y
                    reduction = 50/self.velocity
                    velocity_y = difference_in_y / reduction
                    self.velocity_y = -1 * velocity_y
        else:
            if self.y >= player.right_rect.y and self.y <= player.right_rect.y + 100:
                if self.x + 5 >= player.right_rect.x:
                    self.velocity_x = self.velocity_x * -1
                    middle_y = player.right_rect.y + 50
                    difference_in_y = middle_y - self.y
                    reduction = 50/self.velocity
                    velocity_y = difference_in_y / reduction
                    self.velocity_y = -1 * velocity_y

    def reset(self):
        """
        Resets the ball to its initial position.
        """
        self.x = 637
        self.y = 350
        self.velocity_x = BALL_VELOCITY
        self.velocity_y = 0
