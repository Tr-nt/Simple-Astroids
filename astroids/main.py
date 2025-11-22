import pygame
from constants import *
from player import Player
from logger import log_state

def main():
    #physics
    game_speed = pygame.time.Clock()
    dt = 0


    run_game = True #Flag for gamestate loop

    pygame.init()


    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
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
        #player.update(dt)
        pygame.display.flip() #refreshes screen


if __name__ == "__main__":
    main()
