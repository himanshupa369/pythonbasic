#swap two number without third variable.
a=int(input("enter a:"))
b=int(input("enter b:"))
a=a^b
b=a^b
a=a^b
print("a is",a)
print("b is",b)