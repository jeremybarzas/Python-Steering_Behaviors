'''Vector 2 Math'''

import math

class Vector2(object):
    '''Vector 2 object'''
    def __init__(self, valx, valy):
        '''constructor'''
        self.value = [valx, valy]

    def setx(self, xval):
        ''' set the x value '''
        self.value[0] = xval

    def getx(self):
        ''' get the x value '''
        return self.value[0]

    def sety(self, yval):
        ''' set the y value '''
        self.value[1] = yval

    def gety(self):
        ''' get the y value '''
        return self.value[1]

    def __add__(self, other):
        '''add two vector2s'''
        tmp0 = self.value[0] + other.value[0]
        tmp1 = self.value[1] + other.value[1]
        return Vector2(tmp0, tmp1)

    def __sub__(self, other):
        '''subtract two vector2s'''
        tmp0 = self.value[0] - other.value[0]
        tmp1 = self.value[1] - other.value[1]
        return Vector2(tmp0, tmp1)

    def __mul__(self, other):
        '''multiply a vector by a scalar value'''
        tmp0 = self.value[0] * other
        tmp1 = self.value[1] * other
        return Vector2(tmp0, tmp1)

    def __getitem__(self, key):
        return self.value[key]

    def __eq__(self, other):
        '''vector == to another vector'''
        if self.value[0] == other.value[0] and self.value[1] == other.value[1]:
            return True
        return False

    def magnitude(self):
        '''magnitude of this vector'''
        return math.sqrt((self.value[0] * self.value[0]) + (self.value[1] * self.value[1]))

    def normalise(self):
        '''normalise this vector2'''
        mag = self.magnitude()
        if mag == 0:
            return Vector2(0, 0)
        return Vector2((self.value[0] / mag), (self.value[1] / mag))

    def dotproduct(self, other):
        '''dot product of two vector2s'''
        tmpvec0 = self.normalise()
        tmpvec1 = other.normalise()
        return (tmpvec0.value[0] * tmpvec1.value[0]) + (tmpvec0.value[1] * tmpvec1.value[1])

    def __str__(self):
        return str(self.value[0]) + ', ' + str(self.value[1])
