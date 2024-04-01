#write a program to find product of all digits of a given numbers.
n=int(input("enter a number: "))
sum=1
while n>0:
    b=n%10
    sum=sum*b
    n=n//10
print(sum) 