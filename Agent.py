'''Agent object'''

import pygame
import math
import random
from Vector2 import *
from Seek import *
from Flee import *
from Wander import *

class Agent(object):
    '''Agent object'''

    def __init__(self, linecolor, blitcolor, surface):
        '''constructor'''
        self.position = Vector2(surface.get_width() / 2, surface.get_height() / 2)
        self.acceleration = Vector2(0, 0)
        self.velocity = Vector2(0, 0)
        self.maxvelocity = 400
        self.heading = Vector2(0, 0)
        self.force = Vector2(0, 0)
        self.forces = []
        # Behavior objects
        self.seek = Seek()
        self.flee = Flee()
        self.wander = Wander()
        # Drawing variables
        self.bgsurface = surface
        self.surface = pygame.Surface((20, 20))
        self.surface.fill(blitcolor)
        self.surfacepos = Vector2(self.surface.get_width() / 2, self.surface.get_height() / 2)
        pygame.draw.line(self.surface, linecolor, (self.surface.get_width() * .25, self.surface.get_width() * .5), (self.surface.get_width() *.75, self.surface.get_height() * .5), 1)
        pygame.draw.line(self.surface, linecolor, (self.surface.get_width() * .75, self.surface.get_height() * .5), (self.surface.get_width() * .5, self.surface.get_width() * .25), 1)
        pygame.draw.line(self.surface, linecolor, (self.surface.get_width() * .75, self.surface.get_height() * .5), (self.surface.get_width() * .5, self.surface.get_width() * .75), 1)

    def updateagent(self, deltatime):
        ''' update the agent '''
        self.acceleration = self.force
        self.velocity += self.acceleration * deltatime
        currmag = self.velocity.magnitude()
        if currmag > self.maxvelocity:
            self.velocity = self.velocity.normalise() * self.maxvelocity
        self.position += self.velocity * deltatime
        self.heading = self.velocity.normalise()
        self.clear_force()

    def add_force(self, force):
        ''' add a force to the agents velocity '''
        self.force += force

    def seekit(self, target, mult):
        '''seek the target'''
        seekforce = self.seek.seek(self, target)
        self.add_force(seekforce * mult)
        self.seek.draw(self, target, self.bgsurface)

    def fleefrom(self, target, mult):
        '''flee the target'''
        fleeforce = self.flee.flee(self, target)
        self.add_force(fleeforce * mult)
        self.flee.draw(self, target, self.bgsurface)

    def wandering(self, distance, radius, mult):
        ''' wander around aimlessly '''
        wanderforce = self.wander.wander(self, distance, radius)
        self.add_force(wanderforce * mult)
        self.wander.draw(self, self.bgsurface)

    def clear_force(self):
        ''' clear the force '''
        self.force = Vector2(0, 0)

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

    def __str__(self):
        '''print agents info'''
        return "Postion: " + str(self.position)

    def draw(self, surface):
        ''' draws agent to screen as triangle '''
        # get agent current position
        currpos = self.position
        # calculate the turn angle
        angle = math.atan2(self.heading.gety(), self.heading.getx()) * 180 / math.pi
        if angle < 0:
            angle = 360 + angle
        # make a new surface based on turn angle
        newsurf = pygame.transform.rotate(self.surface, -angle)
        # blit agent onto surface
        surface.blit(newsurf, (int(currpos.getx()), int(currpos.gety())))

    def randompos(self):
        '''randomize agent position'''
        num1 = random.randrange(100, (self.bgsurface.get_width() - 100))
        num2 = random.randrange(100, (self.bgsurface.get_height() - 100))
        self.position = Vector2(num1, num2)

if __name__ == '__main__':
    import Main
    Main.main()
