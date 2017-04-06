'''Unit testing for astar algorithim'''

import pygame
from Agent import Agent
from Vector2 import Vector2

def main():
    '''unit test'''
    pygame.init()
    # set caption in window bar
    pygame.display.set_caption("Steering Behaviors")
    # colors to be used
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    pink = (255, 0, 255)
    black = (0, 0, 0)
    white = (255, 255, 255)
    gray = (125, 125, 125)
    bgcolor = (65, 65, 255)
    darkgray = (25, 25, 25)
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    # agent to be used
    testagent = Agent((screen_width / 2), (screen_height / 2), pink, darkgray)
    # varaibles for while loop
    clock = pygame.time.Clock()
    done = False
    leftclick = False
    rightclick = False
    middleclick = False
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
                    middleclick = False
                # check to see if it was right button
                elif event.button == 3:
                    fleetarget = Vector2(clickpos[0], clickpos[1])
                    leftclick = False
                    rightclick = True
                    middleclick = False
                elif event.button == 2:
                    leftclick = False
                    rightclick = False
                    middleclick = True
            # check to see if a button was pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    testagent.velocity = Vector2(0, 0)
                    leftclick = False
                    rightclick = False
                    middleclick = False
        # fill screen with black
        screen.fill(bgcolor)
        # draw agent to screen
        testagent.draw(screen)
        # create font to be used in drawing text to the screen
        myfont = pygame.font.SysFont("timesnewroman", 28)
        myfont.set_bold(True)
        # set text of each label to be drawn
        fleelabel = myfont.render("Rightclick = Flee", 1, black)
        seeklabel = myfont.render("Leftclick = Seek", 1, black)
        wanderlabel = myfont.render("Middleclick = Wander", 1, black)
        stoplabel = myfont.render("Spacebar = Stop", 1, black)
        fpslabel = myfont.render("FPS: " + str(clock.get_fps()), 1, black)
        # draw text to screen
        screen.blit(fleelabel, (15, 10))
        screen.blit(seeklabel, (15, 40))
        screen.blit(wanderlabel, (15, 70))
        screen.blit(stoplabel, (15, 100))
        screen.blit(fpslabel, (15, 550))
        # logic to control wether it seeks, flees, or wanders
        if leftclick:
            testagent.add_force(testagent.seek(seektarget))
        if rightclick:
            testagent.add_force(testagent.flee(fleetarget))
        if middleclick:
            testagent.add_force(testagent.wander(500, 300) * 33)
        # apply forces calcualated by steering behaviors
        testagent.updateagent(delta)
        testagent.clear_force()
        # update function
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
