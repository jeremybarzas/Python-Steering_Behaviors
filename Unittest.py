'''Unit testing for astar algorithim'''

import pygame

def unit_test():
    '''unit test'''
    pygame.init()
    # set caption in window bar
    pygame.display.set_caption("Steering Behaviors")
    # set window size
    screen = pygame.display.set_mode((800, 600))
    done = False
    while not done:
        # checking events that happen
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True
        # draw these thigns to screen
        screen.fill(white)
        # update function
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    unit_test()
