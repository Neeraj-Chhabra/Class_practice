def square_root(a):
 z=1
 x=a/2 
 while(z==1):
  y = (x + (a/x)) / 2
  if (abs(y-x) < 0.0000001):
   print(x)
   z=2
  else:
   x=y
  # print("new value not final", x)
  # print(y) 

root=int(input("enter the number for the squareroot"))

square_root(root)

