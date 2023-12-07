import pygame
import sys


class Button:
    def __init__(self, x, y, width, height, color, text, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.action = action

    def draw(self, screen, outline=None):
        pygame.draw.rect(screen, self.color, self.rect, 0)

        if outline:
            pygame.draw.rect(screen, outline, self.rect, 2)

        font = pygame.font.Font(None, 36)
        text = font.render(self.text, True, (255, 255, 255))
        text_rect = text.get_rect(
            center=(
                self.rect.x + self.rect.width / 2,
                self.rect.y + self.rect.height / 2,
            )
        )
        screen.blit(text, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


# Start Page
def start_page():
    pygame.init()

    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Start Page")

    clock = pygame.time.Clock()

    start_button = Button(
        300, 200, 200, 50, (0, 128, 255), "Start Game", action=start_game.py
    )

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.is_clicked(pygame.mouse.get_pos()):
                    start_button.action()

        screen.fill((255, 255, 255))
        start_button.draw(screen, (0, 0, 0))

        pygame.display.flip()
        clock.tick(30)
