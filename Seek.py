''' The seek behavior '''

class Seek(object):
    ''' The seek behavior '''

    def seek(self, seeker, target):
        ''' seek the target'''
        currentvelocity = seeker.velocity
        displacement = target - seeker.position
        directiontotarget = displacement.normalise()
        newvelocity = directiontotarget * seeker.maxvelocity
        seekforce = newvelocity - currentvelocity
        seeker.forces.append(seekforce)
        return seekforce
