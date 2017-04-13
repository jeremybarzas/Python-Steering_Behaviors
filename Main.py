'''Unit testing for astar algorithim'''

import pygame
import random
from Agent import Agent
from Vector2 import Vector2

def drawtext(screen, clock):
    '''draw text to screen'''
    white = (255, 255, 255)
    # create font to be used in drawing text to the screen
    myfont = pygame.font.SysFont("timesnewroman", 23)
    # set text of each label to be drawn
    fleelabel = myfont.render("Rightclick = Flee Behavior", 1, white)
    seeklabel = myfont.render("Leftclick = Seek Behavior", 1, white)
    wanderlabel = myfont.render("Middleclick = Wander Behavior", 1, white)
    testlabel = myfont.render("a = All Behaviors", 1, white)
    restartlabel = myfont.render("r = Restart", 1, white)
    stoplabel = myfont.render("Spacebar = Stop", 1, white)
    fpslabel = myfont.render("FPS: " + str(clock.get_fps()), 1, white)
    # draw text to screen
    screen.blit(fleelabel, (15, 10))
    screen.blit(seeklabel, (15, 40))
    screen.blit(wanderlabel, (15, 70))
    screen.blit(testlabel, (15, 100))
    screen.blit(restartlabel, (15, 130))
    screen.blit(stoplabel, (15, 160))
    screen.blit(fpslabel, (15, 550))

def main():
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
    bgcolor = (65, 65, 255)
    linecolor = (255, 0, 255)
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    # create a single agent to be used to test
    testagent = Agent(linecolor, black, screen)
    # multiple agents
    agents = []
    for i in range(0, 6):
        agents.append(Agent(linecolor, black, screen))
        agents[i].randompos()
    # varaibles for while loop
    clock = pygame.time.Clock()
    leftclick = False
    rightclick = False
    middleclick = False
    test = False
    done = False
    while not done:
        # set delta time
        delta = clock.tick(30) / 1000.0
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
                    test = False
                # check to see if it was right button
                elif event.button == 3:
                    fleetarget = Vector2(clickpos[0], clickpos[1])
                    leftclick = False
                    rightclick = True
                    middleclick = False
                    test = False
                elif event.button == 2:
                    leftclick = False
                    rightclick = False
                    middleclick = True
                    test = False
            # check to see if a button was pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    testagent.velocity = Vector2(0, 0)
                    leftclick = False
                    rightclick = False
                    middleclick = False
                    test = False
                    # multiple agents
                    for agent in agents:
                        agent.velocity = Vector2(0, 0)
                if event.key == pygame.K_r:
                    testagent = Agent(linecolor, black, screen)
                    leftclick = False
                    rightclick = False
                    middleclick = False
                    test = False
                    # multiple agents
                    agents = []
                    for i in range(0, 6):
                        agents.append(Agent(linecolor, black, screen))
                        agents[i].randompos()
                if event.key == pygame.K_a:
                    leftclick = False
                    rightclick = False
                    middleclick = False
                    test = True
        # fill screen with black
        screen.fill(bgcolor)
        # draw agent(s) to screen
        testagent.draw(screen)
        # multiple agents
        for agent in agents:
            agent.draw(screen)
        # draw text to the screen
        drawtext(screen, clock)
        # logic to control wether the agent(s) seek, flee, or wanders
        if leftclick:
            # seek function being invoked on a single agent
            testagent.seekit(seektarget, 1)
            # multiple agents
            for agent in agents:
                agent.seekit(seektarget, 1)
        if rightclick:
            # flee function being invoked on a single agent
            testagent.fleefrom(fleetarget, 1)
            # multiple agents
            for agent in agents:
                agent.fleefrom(fleetarget, 1)
        if middleclick:
            # wander function being invoked on a single agent
            testagent.wandering(50, 30, 300)
            # multiple agents
            for agent in agents:
                agent.wandering(50, 30, 300)
        if test:
            # store mouse position to be used as target
            mousepos = pygame.mouse.get_pos()
            target = Vector2(mousepos[0], mousepos[1])
            # seek, flee, and wander functions being invoked at once on a single agent
            testagent.seekit(target, 10)
            testagent.fleefrom(target, 1)
            testagent.wandering(50, 30, 300)
            # multiple agents
            for agent in agents:
                agent.seekit(target, 10)
                agent.fleefrom(target, 1)
                agent.wandering(50, 30, 300)
        # update a single agent
        testagent.updateagent(delta)
        # multiple agents
        for agent in agents:
            agent.updateagent(delta)
        # update function
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
