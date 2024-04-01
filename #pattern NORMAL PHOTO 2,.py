#pattern NORMAL PHOTO 2,
n=int(input("enter the size of pattern: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="  ")
    print(" \r")  