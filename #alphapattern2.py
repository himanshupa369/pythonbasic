#alphapattern2
n=int(input("enter the size of pattern: "))
for i in range(1,n+1):
    v=65
    for j in range(1,n+1):
        print(chr(v),end="  ")
        v=v+1
    print(" \r") 