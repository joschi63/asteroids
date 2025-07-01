import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class CustomText:
    def score_text(screen, points):
        schrift = pygame.font.SysFont(None, 36)
        text = schrift.render(f"Score: {points}", True, (255, 255, 255))
        text_rect = text.get_rect(topright=(SCREEN_WIDTH - 50, 10))
        screen.blit(text, text_rect)