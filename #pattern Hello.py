#pattern Hello
n=int(input("enter the size of pattern: "))
for i in range(1,n+1):
    for j in range(1,n+2):
        print("Hello",end=" ")
    print(" \r")  