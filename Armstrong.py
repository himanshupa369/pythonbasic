#write aprogram to check whether the given number is armstrong or not.
k=int(input("enter the number: "))
sum=0
c=0
while k>0:
    c=c+1
    k=k//10
while k>0:
    rem=k%10
    sum=sum+(rem**c)
    k=k//10
if(k==sum):
    print("The number is armstrong")
else:
    print("The number is not armstrong")
