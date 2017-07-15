def myfunc(x, z, y=10):
  print("x= ",x,"y= ",y,"z= ",z)

myfunc(x=1,y=2,z=5)
a=5
b=6
myfunc(x=a,z=6)
a=1
b=2
c=3
myfunc(y=a,z=b,x=c)

