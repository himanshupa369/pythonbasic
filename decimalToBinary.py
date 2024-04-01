#write a program to convert decimal into binary.
n=int(input("enter the decimal number: "))
print("binary number is")
binary=[]
while n>0:
    rem=n%2
    binary.append(rem)
    n=n//2
binary.reverse()
print(binary)    