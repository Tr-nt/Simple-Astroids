import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x, y, radius): 
        super().__init__(x, y, radius)

    #needs to override pygame.draw.circle
    #redraw surface on screen
    #utilize color as white
    #radius from CircleShape
    #position from center of CircleShape

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt 
        
