import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    player = Player(x, y)
    af = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for i in updatable:
            i.update(dt)
        for a in asteroids:
            for s in shots:
                if a.has_collided(s):
                    a.split()
                    s.kill()
            if a.has_collided(player):
                print("Game over!")
                sys.exit()

        screen.fill("black")
        for i in drawable:
            i.draw(screen)
        pygame.display.flip()
        t = clock.tick(60)
        dt = t / 1000


if __name__ == "__main__":
    main()
