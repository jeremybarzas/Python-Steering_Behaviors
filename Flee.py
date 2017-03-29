''' The flee behavior '''

class Flee(object):
    ''' The flee behavior '''

    def flee(self, fleer, target):
        ''' flee the target'''
        currentvelocity = fleer.velocity
        displacement = target -  fleer.position
        directiontotarget = displacement.normalise()
        newvelocity = directiontotarget *  fleer.maxvelocity
        fleeforce = newvelocity - currentvelocity
        fleer.forces.append(fleeforce)
        return fleeforce
