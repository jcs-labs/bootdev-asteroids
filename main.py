import pygame, sys

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    Player.containers = (updatable, drawable)
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    Shot.containers = (shots, updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidField = AsteroidField()

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        screen.fill("black")

        for a in asteroids:
            if a.collides_with(player):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()

            for s in shots:
                if s.collides_with(a):
                    log_event("asteroid_shot")
                    a.split()
                    s.kill()

        for d in drawable:
            d.draw(screen)

        player.shot_cooldown -= dt
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
