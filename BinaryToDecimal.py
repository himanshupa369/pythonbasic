#write a program to convert binary into decimal.
n=int(input("enter the binary number: "))
p=1
sum=0
while n>0:
    rem=n%10
    s=rem*p
    sum=sum+s
    p=p*2
    n=n//10
print("decimal number is: ",sum)    
