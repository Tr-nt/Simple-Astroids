import pygame
from constants import *

def main():


    run_game = True #Flag for gamestate loop

    pygame.init()


    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while run_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(000)
        pygame.display.flip()


if __name__ == "__main__":
    main()
