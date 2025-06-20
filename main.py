import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shot = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shot,updateable,drawable)

    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color="black")

        updateable.update(dt)

        for obj in asteroids:
            if obj.check_collision(player) == True:
                print("Game over!")
                sys.exit();
        
        for asteroid in asteroids:
            for bullet in shot:
                if bullet.check_collision(asteroid) == True:
                    asteroid.split()
                    bullet.kill()
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = (clock.tick(60) / 1000)


if __name__ == "__main__":
    main()
