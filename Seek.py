''' The seek behavior '''

import pygame
from Vector2 import *

class Seek(object):
    ''' The seek behavior '''

    def __init__(self):
        ''' constructor '''

    def seek(self, agent, target):
        '''seek the target'''
        currentvelocity = agent.velocity
        displacement = target - agent.position
        directiontotarget = displacement.normalise()
        newvelocity = directiontotarget * agent.maxvelocity
        seekforce = newvelocity - currentvelocity
        return seekforce

    def draw(self, agent, target, surface):
        ''' draw seek line to the screen '''
        pygame.draw.line(surface, (0, 255, 0), (agent.position.getx(), agent.position.gety()), (target.getx(), target.gety()), 2)
