import pygame
import random

# Game initialization
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
 
# Bird properties
bird_width = 40
bird_height = 30
bird_x = 150
bird_y = 300
bird_speed = 0

# Pipe properties
pipe_width = 70
pipe_gap = 150
pipe_speed = 3
pipe_list = []


# Score
score = 0
font = pygame.font.Font(None, 36)

def draw_bird(x, y):
    pygame.draw.rect(screen, white, [x, y, bird_width, bird_height])

def draw_pipes(pipe_list):
    for pipe in pipe_list:
        pygame.draw.rect(screen, white, pipe)

def display_score(score):
    score_text = font.render("Score: " + str(score), True, white)
    screen.blit(score_text, (10, 10))

def game_over():
    over_text = font.render("Game Over", True, white)
    screen.blit(over_text, (screen_width/2 - 80, screen_height/2 - 20))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_speed = -8

    # Bird movement
    bird_y += bird_speed
    bird_speed += 1

    # Pipe movement
    for pipe in pipe_list:
        pipe[0] -= pipe_speed

    # Generating new pipes
    if len(pipe_list) == 0 or pipe_list[-1][0] < screen_width - 300:
        pipe_list.append([screen_width, random.randint(50, screen_height - 50 - pipe_gap), pipe_width, screen_height])

    # Removing pipes that are out of screen
    if pipe_list and pipe_list[0][0] < -pipe_width:
        pipe_list.pop(0)
        score += 1

    # Check for collisions
    for pipe in pipe_list:
        if bird_x < pipe[0] + pipe[2] and bird_x + bird_width > pipe[0] and (bird_y < pipe[1] or bird_y + bird_height > pipe[1] + pipe_gap):
            running = False

    if bird_y > screen_height or bird_y < 0:
        running = False
   
    # Refresh screen
    screen.fill(black)
    draw_bird(bird_x, bird_y)
    draw_pipes(pipe_list)
    display_score(score)

    if not running:
        game_over()

    pygame.display.flip()
    clock.tick(60)

