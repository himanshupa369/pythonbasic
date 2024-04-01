#GCD
a=int(input("enter a: "))
b=int(input("enter b: "))
def gcd(a,b):
  if(b == 0): 
   return a
  else: 
   return gcd(b, a % b) 
print("The gcd of a and b is : ", end="") 
print(gcd(a,b))