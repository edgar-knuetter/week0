# Polygon excercise from Week 0

# Name: Margaret Scott (eudaimonious)


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				
bob.delay= 0.01

'''
# This is where you put code to move bob
def square(t, length):
	for i in range(4):
		fd(t, length)
		lt(t)

square(bob, 15)

def polygon(t, length, n):
	for i in range(n):
		fd(t, length)
		lt(t, 360.0/n)

polygon(bob, 30, 6)

def circle(t, r):
	polygon(t, (2*3.14*r)/r, r)

circle(bob, 100)
'''
def arc(t, r, angle):
	n = r
	i = 0
	while 360.0/n*i < angle:
	#for i in range(int(n*angle/360)):
		fd(t, 2*3.14*r/n)
		lt(t, 360.0/n)
		i += 1

arc(bob, 100, 180)

wait_for_user()					
