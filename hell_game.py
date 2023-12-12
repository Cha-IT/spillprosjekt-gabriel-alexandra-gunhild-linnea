import pygame
import random
from pygame import mixer


def hell():
    # Instantiate mixer
    mixer.init()

    # Load audio file
    mixer.music.load("Hell_map/Hellmusikk.mp3")

    # Play the music
    mixer.music.play()

    # Initialize Pygame
    pygame.init()

    # Set up display
    screen_width = 800
    screen_height = 470
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Flappy Bird")

    # Colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    blue = (0, 0, 255)
    grey = (190, 190, 190, 255)
    brown = (138, 51, 36)

    # Clock to control frame rate
    clock = pygame.time.Clock()

    # Bird characteristics
    bird_width = 100
    bird_height = 50
    bird_x = 50
    bird_y = screen_height // 2
    bird_velocity = 17
    gravity = 0.25

    # Load bird image
    bird_image = pygame.image.load("hell_map/raven_bird.png")
    bird_image = pygame.transform.scale(bird_image, (bird_width, bird_height))

    # Pipe characteristics
    pipe_width = 50
    pipe_gap = 225
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
        screen.blit(bird_image, (x, y))

    def draw_pipe(x, y, height):
        pygame.draw.rect(screen, brown, (x, y, pipe_width, height))
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

    def passed_pipe(pipe, bird_x):
        return bird_x > pipe["x"] + pipe_width // 2

    def restart_game():
        global bird_y, bird_velocity, pipes, score, game_over
        bird_y = screen_height // 2
        bird_velocity = 17
        pipes = []
        score = 0
        game_over = False

    # Game loop
    game_over = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if (
                not game_over
                and event.type == pygame.KEYDOWN
                and (event.key == pygame.K_SPACE or event.key == pygame.K_UP)
            ):
                bird_velocity = -6
            if game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                restart_game()

        # Load background image
        background = pygame.image.load("hell_map/hell.jpg")
        background = pygame.transform.scale(background, (screen_width, screen_height))

        # Update bird position
        bird_velocity += gravity
        bird_y += bird_velocity

        # Update pipes
        for pipe in pipes:
            pipe["x"] -= pipe_velocity

        # Add new pipe and update score
        if len(pipes) == 0 or pipes[-1]["x"] < screen_width - 200:
            height = random.randint(50, screen_height - 50 - pipe_gap)
            pipes.append({"x": screen_width, "height": height})

        # Check for passed pipes and update the score
        for pipe in pipes:
            if not pipe.get("passed", False) and passed_pipe(pipe, bird_x):
                pipe["passed"] = True
                score += 1

        # Check for collisions
        if collision_check(pipes, bird_x, bird_y):
            game_over = True

        # Draw the background
        screen.blit(background, (0, 0))

        # Draw everything
        for pipe in pipes:
            draw_pipe(pipe["x"], 0, pipe["height"])
            draw_pipe(
                pipe["x"],
                pipe["height"] + pipe_gap,
                screen_height - pipe["height"] - pipe_gap,
            )
        draw_bird(bird_x, bird_y)
        display_score(score)

        if game_over:
            font = pygame.font.Font(None, 36)
            text = font.render("Game Over. Score: " + str(score), True, grey)
            text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
            screen.blit(text, text_rect)
            restart_text = font.render("Press 'R' to restart", True, grey)
            restart_rect = restart_text.get_rect(
                center=(screen_width // 2, screen_height // 2 + 40)
            )
            screen.blit(restart_text, restart_rect)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
