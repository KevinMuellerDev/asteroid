import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position,
                           self.radius, LINE_WIDTH)

    def split(self) -> int:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 100
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        first_new_asteroid_rotation = self.velocity.rotate(random_angle)
        second_new_asteroid_rotation = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        first_new_asteroid = Asteroid(
            self.position.x, self.position.y, new_radius)
        second_new_asteroid = Asteroid(
            self.position.x, self.position.y, new_radius)

        first_new_asteroid.velocity = first_new_asteroid_rotation * 1.2
        second_new_asteroid.velocity = second_new_asteroid_rotation * 1.2
        return 20

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
