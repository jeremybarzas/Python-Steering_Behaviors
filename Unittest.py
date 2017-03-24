'''Unit test of steering behaviors'''

from Vector2 import Vector2
from Agent import Agent

def unit_test():
    '''Unit test of steering behaviors'''
    jeremy = Agent(Vector2(0, 0))
    target = Agent(Vector2(3, 0))
    print "\nSeek Start"
    print jeremy
    for i in range(0, 3):
        print "\nmove number: " + str(i + 1)
        jeremy.seek(target.position)
        jeremy.apply_forces(1)
        print jeremy
    print "\nSeek End"
    print jeremy
    if jeremy.position == target.position:
        print "\njeremy has reached target"
    else:
        print "\njeremy has not reached target\n"
    print "\nFlee Start"
    print jeremy
    for i in range(0, 3):
        print "\nmove number: " + str(i + 1)
        jeremy.flee(target.position)
        jeremy.apply_forces(1)
        print jeremy
    print "\nFlee End"
    print jeremy


if __name__ == "__main__":
    unit_test()
