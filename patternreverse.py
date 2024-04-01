#patternreverse
n=int(input("enter the size of pattern: "))
for i in range(1,n+1):
    for j in range(n,0,-1):
        print(j,end="  ")
    print(" \r") 