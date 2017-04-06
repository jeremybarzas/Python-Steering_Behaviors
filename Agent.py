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
        self.acceleration = Vector2(0, 0)
        self.velocity = Vector2(0, 0)
        self.maxvelocity = 300
        self.heading = Vector2(0, 0)
        self.force = Vector2(0, 0)
        self.forces = []
        self.surface = pygame.Surface((20, 20))
        self.surface.fill(blitcolor)
        surfacepos = Vector2(self.surface.get_width() / 2, self.surface.get_height() / 2)
        points = [(surfacepos[0] - 1, surfacepos[1] - 6), (surfacepos[0] - 6, surfacepos[1] + 4), (surfacepos[0] + 4, surfacepos[1] + 4)]
        pygame.draw.polygon(self.surface, linecolor, points, 2)

        self.wanderangle = math.pi
        self.previousangle = math.pi

    def updateagent(self, deltatime):
        ''' update the agent '''
        self.acceleration = self.force
        self.velocity += self.acceleration * deltatime
        currmag = self.velocity.magnitude()
        if currmag > self.maxvelocity:
            self.velocity = self.velocity.normalise() * self.maxvelocity
        self.position += self.velocity * deltatime
        self.heading = self.velocity.normalise()

    def add_force(self, force):
        ''' add a force to the agents velocity '''
        self.force += force

    def seek(self, target):
        '''seek the target'''
        currentvelocity = self.velocity
        displacement = target - self.position
        directiontotarget = displacement.normalise()
        newvelocity = directiontotarget * self.maxvelocity
        seekforce = newvelocity - currentvelocity
        return seekforce

    def flee(self, target):
        '''flee the target'''
        currentvelocity = self.velocity
        displacement = target - self.position
        directiontotarget = displacement.normalise()
        newvelocity = directiontotarget * self.maxvelocity
        seekforce = newvelocity - currentvelocity
        fleeforce = seekforce * -1
        return fleeforce

    def wander(self, distance, radius):
        ''' wander around aimlessly '''
        center_circle = self.velocity.normalise()
        center_circle = center_circle * distance
        displacement = Vector2(0, 1) * radius

        # kakalate delta angle
        deltaangle = self.previousangle - self.wanderangle
        # kakalate new angle
        newangle = (random.randrange(0.0, 1.0) * deltaangle) - (deltaangle * .5)
        # store new angle in previous angle
        self.previousangle = newangle
        # set wander angle
        self.wanderangle += newangle

        displacement.setx(math.cos(self.wanderangle) * displacement.magnitude())
        displacement.sety(math.sin(self.wanderangle) * displacement.magnitude())
        wanderforce = center_circle + displacement
        return wanderforce

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
        #  get agent current position
        currpos = self.position
        # calculate the turn angle
        angle = math.atan2(self.heading.gety(), self.heading.getx()) * 180 / math.pi
        if angle < 0:
            angle = 360 + angle
        print self.heading.gety(), ',', self.heading.getx()
        newsurf = pygame.transform.rotate(self.surface, -angle)
        # blit agent onto surface
        surface.blit(newsurf, (int(currpos.getx()), int(currpos.gety())))


if __name__ == '__main__':
    import Main
    Main.main()
