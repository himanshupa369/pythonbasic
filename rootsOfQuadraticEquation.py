#write a program to find roots of quadratic equations.
import math
a=int(input("enter coff. of x^2:"))
b=int(input("enter coff. of x^1:"))
c=int(input("enter coff. of x^0:"))
d=(b**2) - (4 * a * c)
if d<0 :
    print("imaginary roots")
elif d==0:
    e=-b/(2*a)
    print("one real root",e)
else:
    x1= (- b + math.sqrt(d))/(2*a)
    x2= (- b - math.sqrt(d))/(2*a)
    print("roots are:",x1,x2)
