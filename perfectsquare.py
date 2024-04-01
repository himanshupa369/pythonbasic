#perfect square number.
n=int(input("Enter any no:")) 
flag=0 
b=int(n/2) 
for i in range (1,b+1): 
    if i*i==n: 
        flag=1 
        break 
if flag==1: 
    print("Given no. is perfect square of",i) 
else: 
    print("Given no. is not perfect square")