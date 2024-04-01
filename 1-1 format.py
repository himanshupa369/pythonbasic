#alternate 1 and -1.
n=int(input("Enter the number of terms:")) 
for i in range (1,n+1):
    if(i%2==0):
        print("-1",end=" ")
    else:
        print("1",end=" ")    