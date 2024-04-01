#write a program to find sum of all digits of a given numbers.
n=int(input("enter a number: "))
sum=0
while (n!=0):
    b=n%10
    sum=int(sum+b)
    n=n/10
print(sum)