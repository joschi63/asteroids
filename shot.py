import pygame


from circleshape import CircleShape

from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        
    def draw(self, screen):
        return pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), SHOT_RADIUS, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt