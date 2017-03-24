'''Agent object'''

import random
from Vector2 import Vector2

class Agent(object):
    '''Agent object'''

    def __init__(self, pos):
        '''constructor'''
        self.position = pos
        self.velocity = Vector2(0, 1)
        self.maxvelocity = 1
        self.heading = Vector2(0, 0)
        self.target = None
        self.forces = []

    def seek(self, target):
        '''seek the target'''
        currvelo = self.velocity
        displacement = target - self.position
        directiontotarget = displacement.normalise()
        velo = directiontotarget * self.maxvelocity
        seekforce = velo - currvelo
        self.forces.append(seekforce)
        return seekforce

    def flee(self, target):
        '''flee the target'''
        currvelo = self.velocity
        displacement = self.position - target
        directiontotarget = displacement.normalise()
        velo = directiontotarget * self.maxvelocity
        fleeforce = velo - currvelo
        self.forces.append(fleeforce)
        return fleeforce

    def wander(self):
        '''wander around aimlessly'''

        # Start with a random target on the edge of the
        # sphere with a set radius around the agent
        # randomize the jitter vector
        wander_jitter = Vector2(random.randrange(-1, 1), random.randrange(-1, 1))
        print wander_jitter

        # Add a randomised vector to the target, with a
        # magnitude specified by a jitter amount

        # Bring the target back to the radius of the
        # sphere by normalising it and scaling by the radius

        # Add the agents heading, multiplied by an
        # distance, to the target

        wanderforce = wander_jitter
        self.forces.append(wanderforce)
        return wanderforce

    def apply_forces(self, deltatime):
        '''apply forces to agent'''
        for force in self.forces:
            force = force * deltatime
            self.velocity = self.velocity + force
            velocity = self.velocity * deltatime
            self.position = self.position + velocity
            self.heading = self.velocity.normalise()
        self.forces = []

    def __str__(self):
        '''print agents info'''
        return "Postion: " + str(self.position) + "\nVelocity: " + str(self.velocity)

def test(agent):
    sf = agent.seek(Vector2(1, 0))
    print "\nSeek Force: " + str(sf)

    print "\nFlee Force???: " + str(sf * -1)

    ff = agent.flee(Vector2(1, 0))
    print "\nFlee Force: " + str(ff)

if __name__ == '__main__':
    agent = Agent(Vector2(0, 0))
    test(agent)
