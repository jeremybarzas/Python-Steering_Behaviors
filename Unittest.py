'''Unit testing for astar algorithim'''

import pygame

def unit_test():
    '''unit test'''
    pygame.init()
    # set caption in window bar
    pygame.display.set_caption("Steering Behaviors")
    # set window size
    screen = pygame.display.set_mode((800, 600))
    # colors to be used
    black = (0, 0, 0)
    white = (255, 255, 255)
    gray = (125, 125, 125)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    done = False
    while not done:
        # checking events that happen
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True
        # fill screen with black
        screen.fill(black)
        # update function
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    unit_test()
