import pygame
import random
from pygame import mixer


def rosa():
    # Instantiate mixer
    mixer.init()

    # Load audio file
    mixer.music.load("rosaflappybird/Rosamusikk.mp3")

    # Play the music
    mixer.music.play()

    # Initialize Pygame
    pygame.init()

    # Set up display
    screen_width = 700
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Flappy Bird")

    # Colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    blue = (0, 0, 255)

    # Clock to control frame rate
    clock = pygame.time.Clock()

    # Bird characteristics
    bird_width = 60
    bird_height = 80
    bird_x = 50
    bird_y = screen_height // 2
    bird_velocity = 9
    gravity = 0.40
    # Load bird image
    bird_image = pygame.image.load("rosaflappybird/bunny.png")
    bird_image = pygame.transform.scale(bird_image, (bird_width, bird_height))

    # Pipe characteristics
    pipe_width = 50
    pipe_gap = 300
    pipe_velocity = 2
    pipes = []

    # Score
    score = 0
    font = pygame.font.Font(None, 36)

    # Functions
    def display_score(score):
        score_display = font.render(f"Score: {score}", True, white)
        screen.blit(score_display, (10, 10))

    def draw_bird(x, y):
        # Draw bird image
        screen.blit(bird_image, (bird_x, bird_y))

    def draw_pipe(x, y, height):
        pygame.draw.rect(screen, white, (x, y, pipe_width, height))
        pygame.draw.rect(
            screen, white, (x, y + height + pipe_gap, pipe_width, screen_height)
        )

    def collision_check(pipes, bird_x, bird_y):
        for pipe in pipes:
            if bird_x + bird_width > pipe["x"] and bird_x < pipe["x"] + pipe_width:
                if (
                    bird_y < pipe["height"]
                    or bird_y + bird_height > pipe["height"] + pipe_gap
                ):
                    return True
        if bird_y > screen_height or bird_y < 0:
            return True
        return False

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and (
                event.key == pygame.K_SPACE or event.key == pygame.K_UP
            ):
                bird_velocity = -10

        # Update bird position
        bird_velocity += gravity
        bird_y += bird_velocity

        # Update pipes
        for pipe in pipes:
            pipe["x"] -= pipe_velocity

        # Add new pipe
        if len(pipes) > 0 and pipes[0]["x"] < -pipe_width:
            pipes.pop(0)
        if len(pipes) == 0 or pipes[-1]["x"] < screen_width - 200:
            height = random.randint(50, screen_height - 50 - pipe_gap)
            pipes.append({"x": screen_width, "height": height})

        # Check for collisions
        if collision_check(pipes, bird_x, bird_y):
            running = False

            # Draw everything
            display_score(score)  # Update the score display

        for pipe in pipes:
            draw_pipe(pipe["x"], 0, pipe["height"])
            draw_pipe(
                pipe["x"],
                pipe["height"] + pipe_gap,
                screen_height - pipe["height"] - pipe_gap,
            )
        draw_bird(bird_x, bird_y)
        display_score(score)

        # Check for pipe passing
        for pipe in pipes:
            if pipe["x"] == bird_x:
                score += 1

        display_score(score)  # Update the score display

        # Load background image
        background = pygame.image.load("rosaflappybird/pinkbackground.webp")
        background = pygame.transform.scale(background, (screen_width, screen_height))

        # Draw the background
        screen.blit(background, (0, 0))

        # Draw pipes
        for pipe in pipes:
            draw_pipe(pipe["x"], 0, pipe["height"])
            draw_pipe(
                pipe["x"],
                pipe["height"] + pipe_gap,
                screen_height - pipe["height"] - pipe_gap,
            )

        # Draw bird
        draw_bird(bird_x, bird_y)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
