'''Unit testing for astar algorithim'''

import pygame
from Agent import Agent
from Vector2 import Vector2

def unit_test():
    '''unit test'''
    pygame.init()
    # set caption in window bar
    pygame.display.set_caption("Steering Behaviors")
    # colors to be used
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    black = (0, 0, 0)
    white = (255, 255, 255)
    gray = (125, 125, 125)
    # set window size
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    # agent to be used
    agent1 = Agent((screen_width / 2), (screen_height / 2))
    # varaibles for while loop
    clock = pygame.time.Clock()
    done = False
    leftclick = False
    rightclick = False
    while not done:
        delta = clock.tick(60) / 1000.0
        # checking events that happen
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True
            # check to see if mouse button was pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                clickpos = pygame.mouse.get_pos()
                # check to see if it was left button
                if event.button == 1:
                    seektarget = Vector2(clickpos[0], clickpos[1])
                    rightclick = False
                    leftclick = True
                # check to see if it was right button
                elif event.button == 3:
                    fleetarget = Vector2(clickpos[0], clickpos[1])
                    leftclick = False
                    rightclick = True
        # fill screen with black
        screen.fill(black)
        # draw agent to screen as a red triangle
        agent1.draw(screen, red)
        # logic to control wether it seeks or fless
        if leftclick:
            agent1.seek(seektarget)
        elif rightclick:
            agent1.flee(fleetarget)
        # apply forces calcualated by steering behaviors
        agent1.apply_forces(delta)
        # out of bounds check
        if agent1.position.getx() >= screen_width:
            agent1.position.setx(screen_width - 10)
        if agent1.position.getx() <= 0:
            agent1.position.setx(0 + 10)
        if agent1.position.gety() >= screen_height:
            agent1.position.sety(screen_height - 10)
        if agent1.position.gety() <= 0:
            agent1.position.sety(0 + 10)
        # update function
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    unit_test()
