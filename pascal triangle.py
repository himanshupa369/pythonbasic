#pascal triangle Q.19 212.
n=int(input("enter the size of row: "))
for i in range(1,n):
    for j in range(1,i+1):
        if((i+j)%2==0):
            print("1",end=" ")
        else:
            print("0",end=" ")
    print("\r")            