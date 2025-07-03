import pygame

from game_logic.constants import SCREEN_WIDTH, SCREEN_HEIGHT

class CustomText:
    def score_text(screen, points):
        schrift = pygame.font.SysFont(None, 36)
        text = schrift.render(f"Score: {points}", True, (255, 255, 255))
        text_rect = text.get_rect(topright=(SCREEN_WIDTH - 50, 10))
        screen.blit(text, text_rect)

    def lifes_text(screen, lifes):
        schrift = pygame.font.SysFont(None, 36)
        text = schrift.render(f"Lifes: {lifes}", True, (255, 255, 255))
        text_rect = text.get_rect(topleft=(50, 10))
        screen.blit(text, text_rect)