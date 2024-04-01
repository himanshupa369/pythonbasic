#write a program to check whether a given number is amicable or not.
a=int(input("enter the a: "))
b=int(input("enter the b: "))
sum=0
for i in range(1,a+1):
    if a%i ==0:
        sum=sum+i
if sum==b:
    print("given numbers are amicable")
else :
    print("given numbers are not amicable")
