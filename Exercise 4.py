def print_spam():
    print "spam"

def print_lala(lala):
    print "%s" %(lala)

def do_twice(f, arg):
    f(arg)
    f(arg)

do_twice(print_lala, "aiuhf")


def print_twice(d):
    print str(d) * 2


print_twice("lala")

print_twice("spam")
print_twice("spam")

def do_four(funkcja, argument):
    do_twice(funkcja, argument)
    do_twice(funkcja, argument)

do_four(print_lala, "ola")
