import pygame
from constants import *

def main():
    #physics
    game_speed = pygame.time.Clock()
    dt = 0


    run_game = True #Flag for gamestate loop

    pygame.init()


    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while run_game:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(000) #black screen
        game_speed.tick(60) #gives us the frame rate
        dt = game_speed.tick(60)/1000 #will be used later

        pygame.display.flip() #refreshes screen


if __name__ == "__main__":
    main()
