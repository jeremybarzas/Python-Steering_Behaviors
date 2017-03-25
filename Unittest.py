'''Unit test of steering behaviors'''

from Vector2 import Vector2
from Agent import Agent

def unit_test():
    '''Unit test of steering behaviors'''
    # test 1
    jeremy = Agent(Vector2(100,100))
    target = Agent(Vector2(300, 100))
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
    # test 2
    agent = Agent(Vector2(0, 0))
    sf = agent.seek(Vector2(1, 0))
    print "\nSeek Force: " + str(sf)
    print "\nFlee Force???: " + str(sf * -1)
    ff = agent.flee(Vector2(1, 0))
    print "\nFlee Force: " + str(ff)


if __name__ == "__main__":
    unit_test()
