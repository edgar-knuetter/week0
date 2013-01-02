# Polygon excercise from Week 0

# Name: Margaret Scott (eudaimonious)


from TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
bob.delay= 0.01

import math

# This is where you put code to move bob
def square(t, length):
	for i in range(4):
		fd(t, length)
		lt(t)

square(bob, 15)

def polylines(t, length, n, angle): #t is turtle, length is length of line, n is number of lines, angle is angle of turtle turn
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def polygon(t, length, n):
    angle = 360.0/n
    polylines(t, length, n, angle)

polygon(bob, 30, 6)


def circle(t, r):   #r is radius
    circumference = 2*math.pi*r
    num_sides = (circumference / 3) + 1
    seg_length = circumference / num_sides
    angle = 360.0 / num_sides
    polylines(t, seg_length, int(num_sides), angle)

circle(bob, 75)



def arc(t, r, theta): #theta is degrees of arc
    circumference = 2*math.pi*r
    arc_length = theta / 360.0 * circumference
    num_sides = theta / 3
    seg_length = arc_length / num_sides
    angle = theta / num_sides
    polylines(t, seg_length, num_sides, angle)

arc(bob, 100, 180)

wait_for_user()

# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__ == '__main__':
    world = TurtleWorld()

