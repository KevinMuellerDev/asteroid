import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self,position):
        super().__init__(position[0],position[1],SHOT_RADIUS)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius, 2)
    
    def update(self,dt):
        self.position += self.velocity * dt