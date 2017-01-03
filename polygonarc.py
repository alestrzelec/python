from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()


def polygon(t, l, n, angle):
    bob.delay = 0.01
    for i in range(n):
        b = angle / n
        fd(t, l)
        rt(t, b)


def arc(t, r, n, angle):
    l = (6.3 * r) / n
    polygon(t, l, n, angle)

arc(bob, 15, 100, 80.0)
