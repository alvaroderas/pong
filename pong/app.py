"""
Primary module for Pong

This module contains classes and functions that initialize and control the game.
Upon running the application, this program displays the main menu and controls
the screen based on the user's actions. It controls the whole game.

Author: Alvaro Deras
Date: December 30, 2023
"""
from consts import *
from models import *
import pygame, sys

# Initial set up for Pygame features
pygame.init()
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
running = True
clock = pygame.time.Clock()
pygame.display.set_caption("Pong")
icon = pygame.image.load("ping-pong.png")
pygame.display.set_icon(icon)
velocity = BALL_VELOCITY

def get_font(size):
    """
    Returns a pygame font object with the specified size.
    """
    return pygame.font.SysFont("Courier", size)

def controls():
    """
    Displays the controls screen, providing information about the keyboard
    controls for the left and right players in the game.
    """
    while True:
        controls_mouse_pos = pygame.mouse.get_pos()
        screen.fill("black")
        controls_text = get_font(70).render("Controls", True, "White")
        controls_rect = controls_text.get_rect(center=(640, 130))
        screen.blit(controls_text, controls_rect)

        left_text = get_font(50).render("Left Controls", True, "White")
        left_rect = controls_text.get_rect(center = (350, 260))
        screen.blit(left_text, left_rect)


        left_up = get_font(30).render("W KEY = UP", True, "White")
        left_rect_up = controls_text.get_rect(center=(430, 340))
        screen.blit(left_up, left_rect_up)

        left_down = get_font(30).render("S KEY = DOWN", True, "White")
        left_rect_down = controls_text.get_rect(center=(430, 400))
        screen.blit(left_down, left_rect_down)

        right_text = get_font(50).render("Right Controls", True, "White")
        right_rect = controls_text.get_rect(center=(900, 260))
        screen.blit(right_text, right_rect)

        right_up = get_font(30).render("UP ARROW KEY = UP", True, "White")
        right_rect_up = controls_text.get_rect(center=(960, 340))
        screen.blit(right_up, right_rect_up)

        right_down = get_font(30).render("DOWN ARROW KEY = DOWN", True,"White")
        right_rect_down = controls_text.get_rect(center=(930, 400))
        screen.blit(right_down, right_rect_down)

        settings_back = Button(pos=(640, 520), text_input = "Back", font = get_font(65), base_color = "White", hovering_color = "Red")
        settings_back.change_color(controls_mouse_pos)
        settings_back.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if settings_back.check_input(controls_mouse_pos):
                    main_menu()
                    pygame.display.update()
        pygame.display.update()

def multiplayer():
    """
    Initiates the multiplayer mode of the Pong game. It manages the game loop,
    handles player input, and updates the screen accordingly. It includes a
    nested function play_again() that prompts the user to play again or return
    to the main menu after the game ends
    """
    ball = Ball()
    right_score = 0
    left_score = 0

    def play_again():
        """
        Displays a prompt asking the user if they want to play the game again.

        Returns:
        - True if the user chooses to play again.
        - False if the user chooses not to play again.
        """
        while True:
            screen.fill("black")

            play_again_button = Button(pos=(GAME_WIDTH // 4, 360), text_input="Play again?", font=get_font(35), base_color="White", hovering_color="#d7fcd4")
            play_again_mouse_pos = pygame.mouse.get_pos()
            play_again_button.change_color(play_again_mouse_pos)
            play_again_button.update(screen)

            go_to_main_menu = Button(pos=(GAME_WIDTH * 3 / 4, 360), text_input="Return to menu screen?", font=get_font(35), base_color="White", hovering_color="Blue")
            go_to_main_menu.change_color(play_again_mouse_pos)
            go_to_main_menu.update(screen)

            screen.blit(winner_text, (GAME_WIDTH / 2 - 255, GAME_HEIGHT * 1 / 4))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_again_button.check_input(play_again_mouse_pos):
                        player.left_rect = player.left_paddle.get_rect(topleft=(30, 310))
                        player.right_rect = player.right_paddle.get_rect(topleft=(1230, 310))
                        multiplayer()

                    if go_to_main_menu.check_input(play_again_mouse_pos):
                        player.left_rect = player.left_paddle.get_rect(topleft=(30, 310))
                        player.right_rect = player.right_paddle.get_rect(topleft=(1230, 310))
                        main_menu()
            pygame.display.update()

    while True:
        ball.move()
        ball.collision(screen)

        screen.fill("black")

        mid_line = pygame.Surface((15, 15))
        mid_line.fill((255, 255, 255))

        screen.blit(player.left_paddle, player.left_rect)
        screen.blit(player.right_paddle, player.right_rect)

        score_font = get_font(20)
        right_score_counter = score_font.render(f"{right_score}", True, "white")
        left_score_counter = score_font.render(f"{left_score}", True, "white")
        screen.blit(right_score_counter, (GAME_WIDTH * 3/4 - right_score_counter.get_width()//2, 20))
        screen.blit(left_score_counter, (GAME_WIDTH//4 - left_score_counter.get_width()//2, 20))

        if ball.x < 0:
            right_score = right_score + 1
            ball.reset('right')
        if ball.x > 1280:
            left_score = left_score + 1
            ball.reset('left')
        ball.draw(screen)

        mid_y = 0
        for i in range(0, 700):
            screen.blit(mid_line, (630, mid_y))
            mid_y = mid_y + 50
            if mid_y > 700:
                break

        pygame.display.flip()
        pygame.display.update()

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_w]:
            player.left_rect.y -= PADDLE_MOVEMENT
        if keys_pressed[pygame.K_s]:
            player.left_rect.y += PADDLE_MOVEMENT
        if keys_pressed[pygame.K_UP]:
            player.right_rect.y -= PADDLE_MOVEMENT
        if keys_pressed[pygame.K_DOWN]:
            player.right_rect.y += PADDLE_MOVEMENT

        if player.left_rect.y < 0:
            player.left_rect.y = 0
        if player.left_rect.y > 620:
            player.left_rect.y = 620
        if player.right_rect.y < 0:
            player.right_rect.y = 0
        if player.right_rect.y > 620:
            player.right_rect.y = 620

        if left_score >= 7:
            left_winner = True
            winner_text = get_font(50).render("Left Player wins!", True, "white")
            if left_winner:
                play_again()
        if right_score >= 7:
            right_winner = True
            winner_text = get_font(50).render("Right Player wins!", True, "white")
            if right_winner:
                play_again()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def play():
    """
    Displays the main menu screen with options to start a multiplayer game or
    return to the main menu. It handles mouse input for the buttons on the main
    menu.
    """
    while running:
        play_mouse_pos = pygame.mouse.get_pos()
        screen.fill("black")

        multi_button = Button(pos = (640, GAME_HEIGHT/2 - 80), text_input = "Multiplayer", font = get_font(80), base_color = "white", hovering_color = "#d7fcd4")
        multi_button.change_color(play_mouse_pos)
        multi_button.update(screen)

        play_back = Button(pos = (640, 540), text_input = "Back", font = get_font(75), base_color = "White", hovering_color = "Red")
        play_back.change_color(play_mouse_pos)
        play_back.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_back.check_input(play_mouse_pos):
                    main_menu()
                if multi_button.check_input(play_mouse_pos):
                    multiplayer()
        pygame.display.update()


def main_menu():
    """
    Controls the main menu of the Pong game. It displays the game title and
    buttons for starting a game, viewing controls, and quitting the game.
    It handles mouse input for these buttons and transitions to the
    corresponding screens.
    """
    screen.fill("black")
    while running:
        menu_mouse_pos = pygame.mouse.get_pos()
        menu_text = get_font(100).render("Pong", True, "White")
        menu_rect = menu_text.get_rect(center=(640, 100))
        screen.blit(menu_text, menu_rect)

        play_button = Button(pos=(640, 250),  text_input="PLAY", font=get_font(75), base_color="#B5CBFF", hovering_color="White")
        controls_button = Button(pos=(640, 400), text_input="CONTROLS", font=get_font(75), base_color="#B5CBFF", hovering_color="White")
        quit_button = Button(pos=(640, 550), text_input="QUIT", font=get_font(75), base_color="#B5CBFF", hovering_color="White")

        for button in [play_button, controls_button, quit_button]:
            button.change_color(menu_mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.check_input(menu_mouse_pos):
                    play()
                if controls_button.check_input(menu_mouse_pos):
                    controls()
                if quit_button.check_input(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        clock.tick(30)

main_menu()
