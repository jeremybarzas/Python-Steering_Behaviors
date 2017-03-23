'''Vector 2 Math'''
import math

class Vector2(object):
    '''Vector 2 object'''
    def __init__(self, val):
        '''constructor'''
        self.value = val

    def add(self, vec2):
        '''add two vector2s'''
        tmp0 = self.value[0] + vec2.value[0]
        tmp1 = self.value[1] + vec2.value[1]
        return Vector2([tmp0, tmp1])

    def subtract(self, vec2):
        '''subtract two vector2s'''
        tmp0 = self.value[0] - vec2.value[0]
        tmp1 = self.value[1] - vec2.value[1]
        return Vector2([tmp0, tmp1])

    def scalarmult(self, scalar):
        '''multiply a vector by a scalar value'''
        tmp0 = scalar * self.value[0]
        tmp1 = scalar * self.value[1]
        return Vector2([tmp0, tmp1])

    def magnitude(self):
        '''magnitude of this vector'''
        return math.sqrt((self.value[0] * self.value[0]) + (self.value[1] * self.value[1]))

    def normalize(self):
        '''normalize this vector2'''
        mag = self.magnitude()
        return Vector2([(self.value[0] / mag), (self.value[1] / mag)])

    def dotproduct(self, vec2):
        '''dot product of two vector2s'''
        tmpvec0 = self.normalize()
        tmpvec1 = vec2.normalize()
        return (tmpvec0.value[0] * tmpvec1.value[0]) + (tmpvec0.value[1] * tmpvec1.value[1])

    def print_info(self):
        '''prints vector 2 info'''
        print str(self.value[0]) + ', ' + str(self.value[1])
