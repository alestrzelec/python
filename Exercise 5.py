def print_something(x):
    for a in range(x):
        if a<1 or a%4 == 0:
            print "+"
        else:
            print "|"


print_something(5)
