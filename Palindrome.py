#write a program to check given number is palindrome number or not.
n=int(input("Enter number: "))
k=n
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
if k==rev:
    print("given number is palindrome")
else:
    print("given number is not palindrome")