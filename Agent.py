'''Agent object'''

from Vector2 import Vector2

class Agent(object):
    '''Agent object'''

    def __init__(self, posx, posy):
        '''constructor'''
        self.position = Vector2(posx, posy)
        self.velocity = Vector2(0, 0)
        self.maxvelocity = 1
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
        # dafuq
        return self.seek(target) * -1

        # This is the same code as seek but the displacement calculation does self.position first,
        # instead of target first and did not give the correct return value
            # currentvelocity = self.velocity
            # displacement = self.position - target
            # directiontotarget = displacement.normalise()
            # newvelocity = directiontotarget * self.maxvelocity
            # fleeforce = newvelocity - currentvelocity
            # self.forces.append(fleeforce)
            # return fleeforce

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
        return "Postion: " + str(self.position)

def test(testagent):
    '''testing in place'''
    print "\nBEGIN SELFTEST\n"
    print testagent
    print "Seek Force: " + str(testagent.seek(Vector2(1, 0)))
    testagent.apply_forces(1)
    print testagent
    print "\nEND SELFTEST\n"


if __name__ == '__main__':
    agent = Agent(0, 0)
    test(agent)
