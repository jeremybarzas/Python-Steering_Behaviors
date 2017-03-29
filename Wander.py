''' The wander behavior '''

import random
from Vector2 import Vector2

class Wander(object):
    ''' The wander behavior '''
    def __init__(self):
        ''' constructor '''
        self.wander_radius = 0
        self.wander_distance = 0
        self.wander_jitter = Vector2(0, 0)
        self.previous_wander = Vector2(0, 0)

    def wander(self):
        ''' returns a wander force '''
        # Start with a random target on the edge of the
        # sphere with a set radius around the agent

        # Add a randomised vector to the target, with a
        # magnitude specified by a jitter amount

        # Bring the target back to the radius of the
        # sphere by normalising it and scaling by the radius

        # Add the agents heading, multiplied by an
        # distance, to the target

        # We then simply use the target for a Seek behaviour
        