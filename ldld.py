a = [1,2,3]
b = [3,4,8]


#while len(a) > 0:
 #   a.pop()
  #  print "lala"
c = []

for i in range(len(a)):
    c.append(a[i] + b[i])
    print c

for i in range(len(a)):
    a[i] = a[i] + b[i]
    print a