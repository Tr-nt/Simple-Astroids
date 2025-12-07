import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS



class Asteroid(CircleShape):
    def __init__(self, x, y, radius): 
        super().__init__(x, y, radius)

    
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt 
        
    def split(self):
        #TO_DO splitting asteroid into smaller asteroids 
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            
            angle = random.uniform(20, 50)
            neg_angle = -angle 
            
            velocity1 = self.velocity.rotate(angle)
            velocity2 = self.velocity.rotate(neg_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            new_asteroid_positive = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_negative = Asteroid(self.position.x, self.position.y, new_radius)

            new_asteroid_positive.velocity = velocity1 * 1.2
            new_asteroid_negative.velocity = velocity2 * 1.2 

