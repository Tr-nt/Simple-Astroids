import pygame
from constants import *
from player import Player
from shot import Shot
from logger import log_state, log_event
from asteroid import Asteroid
from asteroidfield import AsteroidField


import sys


def main():
    #physics
    game_speed = pygame.time.Clock()
    dt = 0


    run_game = True #Flag for gamestate loop

    pygame.init()


    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    
    asteroid_field = AsteroidField()
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)

     
    
    
    
    while run_game:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(000) #black screen
        for frame in drawable:
            frame.draw(screen)
        #player.draw(screen)
        game_speed.tick(60) #gives us the frame rate
        dt = game_speed.tick(60)/1000 #will be used later
        updatable.update(dt)
        player.shoot_cooldown_timer -= dt
        #player.update(dt)
        for asteroid in asteroids:
            for shot in shots: 
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
            if asteroid.collides_with(player):
                log_event("player_hit")
                run_game = False
                print("GAME OVER!")
                sys.exit()

        pygame.display.flip() #refreshes screen


if __name__ == "__main__":
    main()
