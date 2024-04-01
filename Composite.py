#write a program to check whether the number is composite or not.
n=int(input("enter the number: "))
c=0
for i in range(1,n+1):
    if (n % i) == 0:
        c=c+1
if c>2:
    print("the number is composite")
else :
    print("the number is not composite")