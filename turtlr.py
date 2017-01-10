from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()

t = Turtle()
#l = lenght
def polygon(t, l, n, angle):
    for i in range(n):
        b = angle / n
        fd(t, l)
        rt(t, b)

def arc(t, r, n, angle):
    bob.delay = 0.001
    l = (6.3 * r) / n
    polygon(t, l, n, angle)

def petal(t, r, n, angle):
    for i in range(2):
        arc(t, r, n, angle)
        rt(t, 180.0 - angle)

#petal(t, 50, 200, 10.0)

def flower(t, r, n, angle):
    y = int(360 / angle)
    for i in range(y):
        petal(t, r, n, angle)
        rt(t, 180.0 - angle)

flower(t, 50, 100, 43.0)

