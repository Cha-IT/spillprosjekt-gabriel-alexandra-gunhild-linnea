import pygame
from pygame import mixer
import flappy2
import hell_game
import rosabane

# Initialize Pygame
pygame.init()

# Instantiate mixer
mixer.init()

# Load audio file
mixer.music.load("hell_map/Bakgrunnsmusikk.mp3")

# Play the music on a loop (-1 means loop indefinitely)
mixer.music.play(-1)

# screen resolution
res = (800, 520)

# opens up a window
screen = pygame.display.set_mode(res)

# white color
color = (255, 255, 255)

# light shade of the button
color_light = (170, 170, 170)

# dark shade of the button
color_dark = (100, 100, 100)

# stores the width of the screen into a variable
width = screen.get_width()

# stores the height of the screen into a variable
height = screen.get_height()

# defining a font
smallfont = pygame.font.SysFont("Corbel", 35)

# rendering a text written in this font
text = smallfont.render("quit", True, color)

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()

        # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:
            # if the mouse is clicked on the button the game is terminated
            if (
                width / 2 <= mouse[0] <= width / 2 + 50
                and height / 2 <= mouse[1] <= height / 2 + 40
            ):
                flappy2.christmas()

            if (
                width / 2 + 50 <= mouse[0] <= width / 2 + 100
                and height / 2 <= mouse[1] <= height / 2 + 40
            ):
                hell_game.hell()

            if (
                width / 2 + 100 <= mouse[0] <= width / 2 + 150
                and height / 2 <= mouse[1] <= height / 2 + 40
            ):
                rosabane.rosa()

    # fills the screen with a color
    screen.fill((60, 25, 60))

    # stores the (x, y) coordinates into the variable as a tuple
    mouse = pygame.mouse.get_pos()

    # if mouse is hovered on a button it changes to lighter shade
    if (
        width / 2 <= mouse[0] <= width / 2 + 50
        and height / 2 <= mouse[1] <= height / 2 + 40
    ):
        pygame.draw.rect(screen, color_light, [width / 2, height / 2, 50, 40])
    else:
        pygame.draw.rect(screen, color_dark, [width / 2, height / 2, 50, 40])

    if (
        width / 2 + 50 <= mouse[0] <= width / 2 + 100
        and height / 2 <= mouse[1] <= height / 2 + 40
    ):
        pygame.draw.rect(screen, color_light, [width / 2 + 50, height / 2, 50, 40])
    else:
        pygame.draw.rect(screen, color_dark, [width / 2 + 50, height / 2, 50, 40])

    if (
        width / 2 + 100 <= mouse[0] <= width / 2 + 150
        and height / 2 <= mouse[1] <= height / 2 + 40
    ):
        pygame.draw.rect(screen, color_light, [width / 2 + 100, height / 2, 50, 40])
    else:
        pygame.draw.rect(screen, color_dark, [width / 2 + 100, height / 2, 50, 40])

    # superimposing the text onto our button
    screen.blit(text, (width / 2 + 50, height / 2))

    # updates the frames of the game
    pygame.display.update()
