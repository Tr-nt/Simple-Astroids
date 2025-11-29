import pygame
from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from constants import PLAYER_SHOT_SPEED
from constants import PLAYER_SHOOT_COOLDOWN_SECONDS

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown_timer = 0
    
    # TO-DO: implement cooldown timer for shooting

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, 'white',self.triangle(), 2)

    def rotate_player(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        return self.rotation

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate_player(dt)
        if keys[pygame.K_d]:
            self.rotate_player(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            # TO-DO: implement cooldown timer for shooting
            if self.shoot_cooldown_timer <= 0:
                self.shoot()
                self.shoot_cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
            else:
                pass


    def shoot(self, interval=0):
        shot = Shot(self.position.x, self.position.y) 
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
        

    

