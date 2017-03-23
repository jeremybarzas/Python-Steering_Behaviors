'''Agent object'''

class Agent(object):
    '''Agent object'''

    def __init__(self):
        '''constructor'''
        self.position = None
        self.velocity = None
        self.maxvelocity = 1
        self.heading = None
        self.target = None

    def seek(self, target, deltatime):
        '''seek the target'''
        # calculate seek force
        tmpvec = target.position.substract(self.position)
        tmpvec = tmpvec.normalize()
        tmpvec = tmpvec.scalarmult(self.maxvelocity)
        seekforce = tmpvec.subtract(self.velocity)
        # apply seek force
        seekforce = seekforce.scalarmult(deltatime)
        self.velocity = self.velocity.add(seekforce)
        velocity = self.velocity.scalarmult(deltatime)
        self.position = self.position.add(velocity)
        self.heading = self.velocity.normalize()

    def flee(self, target, deltatime):
        '''flee the target'''
        # calculate flee force
        tmpvec = self.position.substract(target.position)
        tmpvec = tmpvec.normalize()
        tmpvec = tmpvec.scalarmult(self.maxvelocity)
        fleeforce = tmpvec.subtract(self.velocity)
        # apply flee force
        fleeforce = fleeforce.scalarmult(deltatime)
        self.velocity = self.velocity.add(fleeforce)
        velocity = self.velocity.scalarmult(deltatime)
        self.position = self.position.add(velocity)
        self.heading = self.velocity.normalize()
