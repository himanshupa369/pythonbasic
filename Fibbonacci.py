#write a program to print fibbonacci series of a number.
n=int(input("enter the number: "))
a=0
b=1
if n==0:
    print(a)
if n==1:
    print(a)
    print(b)
if n>1:
    print(a)
    print(b)
    for i in range(1,n-1):
        c=a+b
        print(c)
        a=b
        b=c          
