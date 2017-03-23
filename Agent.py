'''Agent object'''

from Vector2 import Vector2

class Agent(object):
    '''Agent object'''

    def __init__(self, pos):
        '''constructor'''
        self.position = pos
        self.velocity = Vector2([0, 0])
        self.maxvelocity = 1
        self.heading = None
        self.target = None

    def seek(self, target):
        '''seek the target'''
        tmpvec = target.position.substract(self.position)
        tmpvec = tmpvec.normalize()
        tmpvec = tmpvec.scalarmult(self.maxvelocity)
        seekforce = tmpvec.subtract(self.velocity)
        return seekforce

    def flee(self, target):
        '''flee the target'''
        tmpvec = self.position.substract(target.position)
        tmpvec = tmpvec.normalize()
        tmpvec = tmpvec.scalarmult(self.maxvelocity)
        fleeforce = tmpvec.subtract(self.velocity)
        return fleeforce

    def apply_forces(self, forces, deltatime):
        '''apply forces to agent'''
        for force in forces:
            force = force.scalarmult(deltatime)
            self.velocity = self.velocity.add(force)
            velocity = self.velocity.scalarmult(deltatime)
            self.position = self.position.add(velocity)
            self.heading = self.velocity.normalize()

    def print_info(self):
        '''print agents info'''
        print "\nPostion:"
        self.position.print_info()
        print "Velocity: "
        self.velocity.print_info()
        