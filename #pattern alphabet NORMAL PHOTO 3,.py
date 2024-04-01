#pattern alphabet NORMAL PHOTO 3,
n=int(input("enter the size of pattern: "))
v=64
for i in range(1,n+1):
    v=v+1
    for j in range(1,i+1):
        print(chr(v),end="  ")
    print(" \r")  