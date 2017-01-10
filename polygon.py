from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()

t = Turtle()
def polygon(t, l, n):
    for i in range(n):
        b = 360.0 / n
        fd(t, l)
        rt(t, b)

def circle(t, r, n):
    l = (6.3 * r) / n
    bob.delay = 0.01
    polygon(t, l, n)

circle(bob, 50, 100)