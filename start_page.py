import pygame
import sys
import flappy2
import hell_game
import rosabane

# initializing the constructor
pygame.init()

# screen resolution
res = (800, 470)

# opens up a window
screen = pygame.display.set_mode(res)

# white color
color = (255, 255, 255)

# light shade of the button
color_light = (170, 170, 170)

# blue shade of the button
color_blue = (80, 137, 181)

# stores the width of the
# screen into a variable
width = screen.get_width()

# stores the height of the
# screen into a variable
height = screen.get_height()

# defining a font
smallfont = pygame.font.SysFont("Calibri", 35)

# rendering a text written in
# this font
text = smallfont.render("Hell", True, color)
text2 = smallfont.render("Christmas", True, color)
text3 = smallfont.render("Rosabane", True, color)

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()

        # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:
            # if the mouse is clicked on the
            # button the game is terminated

            if (
                width / 2 - 90 <= mouse[0] <= width / 2 + 90
                and height / 2 - 80 <= mouse[1] <= height / 2 - 30
            ):
                hell_game.hell()

            if (
                width / 2 - 90 <= mouse[0] <= width / 2 + 90
                and height / 2 <= mouse[1] <= height / 2 + 50
            ):
                flappy2.christmas()

            if (
                width / 2 - 90 <= mouse[0] <= width / 2 + 90
                and height / 2 + 30 <= mouse[1] <= height / 2 + 80
            ):
                rosabane.rosa()

    # Load background image
    background = pygame.image.load("./start_page_background.webp")
    background = pygame.transform.scale(background, (width, height))

    # Draw the background
    screen.blit(background, (0, 0))

    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()

    # if mouse is hovered on a button it
    # changes to lighter shade
    if (
        width / 2 <= mouse[0] <= width / 2
        and height / 2 - 80 <= mouse[1] <= height / 2 - 80
    ):
        pygame.draw.rect(
            screen, color_light, [width / 2 - 90, height / 2 - 80, 180, 50]
        )
    else:
        pygame.draw.rect(
            screen, color_blue, [width / 2 - 90, height / 2 + -80, 180, 50]
        )

    if width / 2 <= mouse[0] <= width / 2 and height / 2 <= mouse[1] <= height / 2:
        pygame.draw.rect(screen, color_light, [width / 2 - 90, height / 2, 180, 50])
    else:
        pygame.draw.rect(screen, color_blue, [width / 2 - 90, height / 2, 180, 50])

    if (
        width / 2 <= mouse[0] <= width / 2
        and height / 2 + 80 <= mouse[1] <= height / 2 + 80
    ):
        pygame.draw.rect(
            screen, color_light, [width / 2 - 90, height / 2 + 80, 180, 50]
        )
    else:
        pygame.draw.rect(screen, color_blue, [width / 2 - 90, height / 2 + 80, 180, 50])

    # superimposing the text onto our button
    screen.blit(text, (width / 2 - 75, height / 2 - 70))
    screen.blit(text2, (width / 2 - 75, height / 2 + 10))
    screen.blit(text3, (width / 2 - 75, height / 2 + 91))

    # updates the frames of the game
    pygame.display.update()
