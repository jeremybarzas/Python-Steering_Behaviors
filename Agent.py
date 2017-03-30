'''Agent object'''

import pygame
from Vector2 import Vector2

class Agent(object):
    '''Agent object'''

    def __init__(self, posx, posy):
        '''constructor'''
        self.position = Vector2(posx, posy)
        self.velocity = Vector2(0, 0)
        self.maxvelocity = 100
        self.heading = Vector2(0, 0)
        self.forces = []
        self.previousforces = []

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

    def draw(self, surface, color):
        ''' draws agent to screen as triangle '''
        centeroid = self.position
        points = [(centeroid.getx(), centeroid.gety() - 5), (centeroid.getx() - 5, centeroid.gety() + 5), (centeroid.getx() + 5, centeroid.gety() + 5)]
        pygame.draw.polygon(surface, color, points, 2)
        return 1


def test():
    '''testing in place'''
    print "\nBEGIN SELFTEST\n"
    red = (255, 0, 0)
    black = (0, 0, 0)
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    testagent = Agent((screen_width / 2), (screen_height / 2))
    testagent.draw(screen, red)
    print "\nEND SELFTEST\n"


if __name__ == '__main__':
    test()
