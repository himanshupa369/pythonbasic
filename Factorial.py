#write a program to print factorial of given numbers.
n=int(input("enter the n: "))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)    