import pygame
import sys

from game_logic.constants import *
from game_logic.player import Player
from game_logic.asteroid import Asteroid
from game_logic.asteroidfield import AsteroidField
from game_logic.shot import Shot

from text.customtext import CustomText as cT

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    points = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    schrift = pygame.font.SysFont(None, 36)
    text = schrift.render(f"Score: {points}", True, (255, 255, 255))

    text_rect = text.get_rect(topright=(SCREEN_WIDTH - 50, 10))

   

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0, 0, 0))
            
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                sys.exit(f"Game Over! \nDein Score waren {points} Punkte")
            
            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()
                    points += 1
                    cT.score_text(screen, points)
                    continue
        
                
        cT.score_text(screen, points)
        for drawl in drawable:
            drawl.draw(screen) 

        
         # Draw the text on the screen
        pygame.display.flip()  # Update the display

        clock.tick(60)
        dt = clock.get_time() / 1000.0

    """
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    """
if __name__ == "__main__":
    main()
