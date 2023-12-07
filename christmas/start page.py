import pygame

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 470
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

# Colors
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)

# Clock to control frame rate
clock = pygame.time.Clock()

# Load background image
background = pygame.image.load("christmas/christmas_background.jpg")
background = pygame.transform.scale(background, (screen_width, screen_height))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(white)

    # Draw the background
    screen.blit(background, (0, 0))

    # Draw the first box
    pygame.draw.rect(screen, red, (100, 90, 150, 100))
    font = pygame.font.Font(None, 36)
    text = font.render("PINK", True, black)
    screen.blit(text, (175 - text.get_width() // 2, 140 - text.get_height() // 2))

    # Draw the second box
    pygame.draw.rect(screen, red, (325, 90, 150, 100))
    text = font.render("JUL", True, black)
    screen.blit(text, (400 - text.get_width() // 2, 140 - text.get_height() // 2))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
