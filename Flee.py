''' The flee behavior '''

import pygame

class Flee(object):
    ''' The flee behavior '''

    def __init__(self):
        ''' constructor '''

    def flee(self, agent, target):
        '''flee the target'''
        currentvelocity = agent.velocity
        displacement = target - agent.position
        directiontotarget = displacement.normalise()
        newvelocity = directiontotarget * agent.maxvelocity
        seekforce = newvelocity - currentvelocity
        fleeforce = seekforce * -1
        return fleeforce

    def draw(self, agent, target, surface):
        ''' draw seek line to the screen '''
        pygame.draw.line(surface, (255, 0, 0), (agent.position.getx(), agent.position.gety()), (target.getx(), target.gety()), 2)
