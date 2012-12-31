# Hello excercise from Week 0

# Name: Margaret Scott (eudaimonious)


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				

# This is where you put code to move bob

#H starting position
pu(bob)
lt(bob)
fd(bob, 100)
lt(bob)
fd(bob, 150)
pd(bob)
lt(bob)

#H
fd(bob, 100)
lt(bob)
lt(bob)
fd(bob, 50)
rt(bob)
fd(bob, 25)
rt(bob)
fd(bob, 50)
lt(bob)
lt(bob)
fd(bob, 100)

#E starting position
pu(bob)
rt(bob)
fd(bob, 15)
pd(bob)

#E
fd(bob, 25)
bk(bob, 25)
rt(bob)
fd(bob, 50)
lt(bob)
fd(bob, 25)
bk(bob, 25)
rt(bob)
fd(bob, 50)
lt(bob)
fd(bob, 25)

#L(1) starting position
pu(bob)
fd(bob, 15)
lt(bob)
fd(bob, 100)
pd(bob)

#L(1)
bk(bob, 100)
rt(bob)
fd(bob, 25)

#L(2) starting position
pu(bob)
fd(bob, 15)
lt(bob)
fd(bob, 100)
pd(bob)

#L(2)
bk(bob, 100)
rt(bob)
fd(bob, 25)

#O starting position
pu(bob)
fd(bob, 15)
lt(bob)
fd(bob, 100)
pd(bob)

#O
bk (bob, 100)
rt(bob)
fd(bob, 25)
lt(bob)
fd(bob, 100)
lt(bob)
fd(bob, 25)

#end position
pu(bob)
bk(bob, 35)
lt(bob)
fd(bob, 100)
lt(bob)

wait_for_user()					
