'''Unit test of steering behaviors'''

from Vector2 import Vector2
from Agent import Agent

def unit_test():
    '''Unit test of steering behaviors'''
    jeremy = Agent(Vector2([400, 300]))
    jeremy.print_info()
    forces = [Vector2([1, 0])]
    jeremy.apply_forces(forces, 1)
    jeremy.print_info()

if __name__ == "__main__":
    unit_test()
