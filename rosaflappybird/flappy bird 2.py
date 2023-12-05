import pygame
import random

pygame.init()

# Screen dimensions
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Bird attributes
bird_x = 50
bird_y = 300
bird_width = 20
bird_height = 20
bird_velocity = 0 

# Gravity and jump force
gravity = 0.30
jump_force = 6

# Pipe attributes
pipe_width = 50
pipe_velocity = 3
pipe_gap = 200
pipe_list = []

# Game variables
game_over = False
score = 0
font = pygame.font.Font(None, 36)

# Function to draw the bird
def draw_bird():
    pygame.draw.rect(screen, blue, (bird_x, bird_y, bird_width, bird_height))


# Function to draw the pipes
def draw_pipes():
    for pipe in pipe_list:
        pygame.draw.rect(screen, green, (pipe[0], 0, pipe_width, pipe[1]))
        pygame.draw.rect(screen, green, (pipe[0], pipe[1] + pipe_gap, pipe_width, screen_height))

# Function to move the pipes
def move_pipes():
    for pipe in pipe_list:
        pipe[0] -= pipe_velocity

# Function to generate pipes
def create_pipe():
    random_pos = random.randint(50, screen_height - 50 - pipe_gap)
    pipe_list.append([screen_width, random_pos])

# Function to check collision
def check_collision():
    for pipe in pipe_list:
        if pipe[0] <= bird_x + bird_width and pipe[0] + pipe_width >= bird_x:
            if bird_y <= pipe[1] or bird_y + bird_height >= pipe[1] + pipe_gap:5
                return True
        if bird_y <= 0 or bird_y + bird_height >= screen_height:
            return True
    return False

# ... (previous code remains the same)

# Function to display score
def display_score(score):
    score_text = font.render(f"Score: {str(score)}", True, black)
    screen.blit(score_text, [10, 10])

# Game loop
clock = pygame.time.Clock()
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = -jump_force

    screen.fill(white)

    bird_velocity += gravity
    bird_y += bird_velocity

    if len(pipe_list) == 0 or pipe_list[-1][0] <= screen_width - 200:
        create_pipe()

    pipes_to_remove = []
    add_score = False
    for pipe in pipe_list:
        pipe[0] -= pipe_velocity
        if pipe[0] < bird_x and not pipe[3]:
            add_score = True
            pipe[3] = True
        if pipe[0] < -pipe_width:
            pipes_to_remove.append(pipe)

    if add_score:
        score += 1

    for pipe in pipes_to_remove:
        pipe_list.remove(pipe)

    move_pipes()
    draw_pipes()
    draw_bird()

    display_score(score)

    game_over = check_collision()

    pygame.display.update()
    clock.tick(60) 

#Game loop
clock = pygame.time.Clock()
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = -jump_force

    screen.fill(white)

    bird_velocity += gravity
    bird_y += bird_velocity

    if len(pipe_list) == 0 or pipe_list[-1][0] <= screen_width - 200:
        create_pipe()

    move_pipes()
    draw_pipes()
    draw_bird()

    game_over = check_collision()

    pygame.display.update()
    clock.tick(60)
    

pygame.quit()
 
