#Q.11 206 
lower=int(input("Enter the lower range:"))
upper=int(input("Enter the upper range:"))
sum=0
for i in range (lower,upper+1):
    if(i%7==0 ):
        sum=sum+i
        print(i)
print(sum)
