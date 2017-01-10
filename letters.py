from swampy.TurtleWorld import *
world = TurtleWorld()

bob = Turtle()
#l = lenght
#a = angle
def letter_a(t,l, a):
    lt(t, 90)
    rt(t, a)
    fd(t, l)
    rt(t, a)
    fd(t, l)
    pu
    bk(t, l / 3)
    pd
    lt(t, a * 2)
    fd (t, l / 3)

letter_a(bob, 50, 90)