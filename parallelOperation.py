#parallel operation on series of naturl numbers.
def seriesDifference(n):
    sum1=0
    sum2=0
    for i in range(1,n+1):
        if(i%2==0):
            sum1=sum1+i
        else:
            sum2=sum2+i
    sum=sum1-sum2
    print(sum)  
def seriesEvenSum(n):
    sum1=0
    for i in range(1,n+1):
        if(i%2==0):
            sum1=sum1+i
    print(sum1)
def reverseSum(n):
    sum1=0
    for i in range(1,n+1):
        sum1=sum1+1/i
    print(sum1)
def reverseDifference(n):
    sum1=0
    sum2=0
    for i in range(1,n+1):
        if(i%2==0):
            sum1=sum1+1/i
        else:
            sum2=sum2+1/i
    sum=sum1-sum2
    print(sum)
def reverseEvenSum(n):
    sum1=0
    for i in range(1,n+1):
        if(i%2==0):
            sum1=sum1+1/i
    print(sum1)
z=int(input("enter the number: "))
seriesDifference(z)
print()
seriesEvenSum(z)
print()
reverseSum(z)
print()
reverseDifference(z)
print()
reverseEvenSum(z)
print()