#write a program to check given number is prime or not with break.
def prime(n):
    count=0
    for i in range(1,n+1):
        if(n%i==0):
            count=count+1;
            if(count>=3):
                break
    if(count==2):
        print("n is prime number")        
    else:
        print("n is not prime number")
#driven code
n=int(input("enter the number n: "))    
prime(n)
              


        
