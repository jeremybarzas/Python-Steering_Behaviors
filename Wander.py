''' The wander behavior '''

import math
import random
import pygame
from Vector2 import Vector2


class Wander(object):
    ''' The wander behavior '''

    def __init__(self):
        ''' constructor '''
        self.wanderangle = math.pi
        self.previousangle = math.pi
        self.center_circle = Vector2(0, 0)
        self.displacement = Vector2(0, 0)
        self.wandertemp = Vector2(0, 0)

    def wander(self, agent, distance, radius):
        ''' wander around aimlessly '''
        self.center_circle = agent.velocity.normalise()
        self.center_circle = self.center_circle * distance
        self.displacement = Vector2(0, 1) * radius
        deltaangle = self.previousangle - self.wanderangle
        newrandom = random.randrange(0.0, 1.0)
        newangle = (newrandom * deltaangle) - (deltaangle * .5)
        self.previousangle = newangle
        self.wanderangle = self.wanderangle + newangle

        # ========== DEBUG STUFF ==========
        print "wander angle: ", self.wanderangle

        # this makes the math domain error not occur
        if self.wanderangle == float("inf"):
            self.wanderangle = math.pi
            self.previousangle = math.pi

        self.displacement.setx(math.cos(self.wanderangle) * self.displacement.magnitude())
        self.displacement.sety(math.sin(self.wanderangle) * self.displacement.magnitude())
        wanderforce = self.center_circle + self.displacement
        self.wandertemp = wanderforce
        return wanderforce

    def draw(self, agent, surface):
        '''used to draw wander circle and lines'''
        circle_center = agent.position + self.wandertemp
        displacement = circle_center + self.displacement
        pygame.draw.line(surface, (255, 255, 255), (agent.position.getx(), agent.position.gety()), (circle_center.getx(), circle_center.gety()), 2)
        pygame.draw.line(surface, (0, 0, 0), (circle_center.getx(), circle_center.gety()), (displacement.getx(), displacement.gety()), 2)
