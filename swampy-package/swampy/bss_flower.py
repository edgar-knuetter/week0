# Flower excercise (4.2) from Week 0

# Name: Margaret Scott (eudaimonious)

from TurtleWorld import *
import math
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def arc(t, r, angle):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    lt(t, step_angle/2)
    polyline(t, n, step_length, step_angle)
    rt(t, step_angle/2)

def petal(t, r, theta):
  """Uses a turtle(t) to draw a flower petal
  that of radius (r) and circle fraction (theta)."""
  for i in range (2):
    arc(t, r, theta)
    lt(t, 180-theta)

def flower(t, r, theta, num_petals):
  """Draws num_petals given to fill 360 degree space."""
  for i in range(num_petals):
    petal(t, r, theta)
    lt(t, 360.0/num_petals)

def move(t, distance):
  """Moves turtles without drawing."""
  pu(t)
  fd(t, distance)
  pd(t)

# This is where you put code to move bob

move(bob, -100)
flower(bob, 60, 60, 7)

move(bob, 100)
flower(bob, 40, 80, 10)

move(bob, 100)
flower(bob, 140, 20, 20)
'''
arc(bob, 80, 100)
lt(bob)
arc(bob, 80, 100)
lt(bob)
arc(bob, 80, 100)
'''



wait_for_user()

