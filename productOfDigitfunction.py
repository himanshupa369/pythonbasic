def productOfDigit(n):
    sum = 1
    while n > 0:
        sum *= n % 10
        n //= 10
    print(sum)

n=int(input("enter the n: "))
productOfDigit(n)