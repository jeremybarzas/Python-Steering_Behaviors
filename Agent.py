'''Agent object'''

import pygame
import math
import random
from Vector2 import Vector2

class Agent(object):
    '''Agent object'''

    def __init__(self, posx, posy, linecolor, blitcolor):
        '''constructor'''
        self.position = Vector2(posx, posy)
        self.velocity = Vector2(0, 0)
        self.maxvelocity = 750
        self.heading = Vector2(0, 0)
        self.forces = []
        self.previousforces = []
        self.surface = pygame.Surface((20, 20))
        sur = self.surface
        sur.fill(blitcolor)
        currpos = Vector2(sur.get_width() / 2, sur.get_height() / 2)
        points = [(currpos[0] - 1, currpos[1] - 6), (currpos[0] - 6, currpos[1] + 4), (currpos[0] + 4, currpos[1] + 4)]
        pygame.draw.polygon(self.surface, linecolor, points, 2)

    def seek(self, target):
        '''seek the target'''
        currentvelocity = self.velocity
        displacement = target - self.position
        directiontotarget = displacement.normalise()
        newvelocity = directiontotarget * self.maxvelocity
        seekforce = newvelocity - currentvelocity
        self.forces.append(seekforce)
        return seekforce

    def flee(self, target):
        '''flee the target'''
        currentvelocity = self.velocity
        displacement = target - self.position
        directiontotarget = displacement.normalise()
        newvelocity = directiontotarget * self.maxvelocity
        seekforce = newvelocity - currentvelocity
        fleeforce = seekforce * -1
        self.forces.append(fleeforce)
        return fleeforce

    def wander(self, distance, radius):
        ''' wander around aimlessly '''
        # Start with a random target on the edge of the
        # sphere with a set radius around the agent

        # Add a randomised vector to the target, with a
        # magnitude specified by a jitter amount

        # Bring the target back to the radius of the
        # sphere by normalising it and scaling by the radius

        # Add the agents heading, multiplied by an
        # distance, to the target

        center_circle = self.velocity.normalise()
        center_circle = center_circle * distance
        displacement = Vector2(0, 1)
        wanderangle = wanderangle + (random.randrange(0.0, 1.0) * 1) - (1 * .5)
        displacement.setx(math.cos(wanderangle) * displacement.magnitude())
        displacement.sety(math.sin(wanderangle) * displacement.magnitude())

    def apply_forces(self, deltatime):
        '''apply forces to agent'''
        tmpforce = Vector2(0, 0)
        for force in self.forces:
            tmpforce = tmpforce + force
        tmpforce = tmpforce * deltatime
        self.velocity = self.velocity + tmpforce
        currmag = self.velocity.magnitude()
        if currmag > self.maxvelocity:
            self.velocity = self.velocity.normalise() * self.maxvelocity
        velocity = self.velocity * deltatime
        self.position = self.position + velocity
        self.heading = self.velocity.normalise()
        self.clear_forces()

    def clear_forces(self):
        ''' clear the forces list '''
        for force in self.forces:
            self.forces.pop()
        self.forces = []

    def __str__(self):
        '''print agents info'''
        return "Postion: " + str(self.position)

    def draw(self, surface):
        ''' draws agent to screen as triangle '''
        currpos = self.position
        surface.blit(self.surface, (int(currpos.getx()), int(currpos.gety())))


if __name__ == '__main__':
    import Main
    Main.main()
    