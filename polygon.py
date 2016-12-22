from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()

t = Turtle()
def polygon(t, lenght, n):
    for i in range(n):
        b = 360 / n
        fd(t, lenght)
        rt(t, b)

polygon(bob, 100, 3)
