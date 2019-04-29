def square_root(a):
 z=1
 x=a/2 
 while(z==1):
  y = (x + (a/x)) / 2
  if (abs(y-x) < 0.0000001):
   print(x)
   z=2
   return(x)
  else:
   x=y
  # print("new value not final", x)
  # print(y) 

def test_square_root(a):
 return(math.sqrt(a))

root=int(input("enter the number for the squareroot"))
import math
d=square_root(root)
print(type(d))
b=test_square_root(root)
print(type(b))
c=abs(d-b)
print(type(c))
print(root,"\t", d, "\t", b ,"\t", c) 

 
