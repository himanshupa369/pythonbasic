#write a program to print reverse of a number.
def reverseOfNumberDigit(n):
    rev=0
    while(n>0):
        rem=n%10
        rev=rev*10+rem
        n=n//10
    print("Reverse of the number:",rev)

#driven function
x=int(input("Enter number: "))
reverseOfNumberDigit(x)