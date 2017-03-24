'''Unit test of steering behaviors'''

from Vector2 import Vector2
from Agent import Agent

def unit_test():
    '''Unit test of steering behaviors'''
    jeremy = Agent(Vector2([0, 0]))
    target = Agent(Vector2([3, 0]))
    print "\nStart location"
    jeremy.print_info()
    for i in range(0, 3):
        print "\nmove number: " + str(i + 1)
        jeremy.seek(target)
        jeremy.apply_forces(1)
        jeremy.print_info()
    print "\nEnd location"
    jeremy.print_info()
    if jeremy.position == target.position:
        print "\njeremy has reached target"
    else:
        print "\njeremy has not reached target\n"
    print "\nStart location"
    jeremy.print_info()
    for i in range(0, 3):
        target1 = Agent(jeremy.wander())
        print "\nmove number: " + str(i + 1)
        jeremy.seek(target1)
        jeremy.apply_forces(1)
        jeremy.print_info()
    print "\nEnd location"
    jeremy.print_info()


if __name__ == "__main__":
    unit_test()
