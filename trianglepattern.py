# number pyramid pattern
size = int(input("enter size of pattern:   "))
for i in range(size):
    # print spaces
    for j in range(size - i - 1):
        print(" ", end=" ")
    # print numbers
    for k in range(2 * i + 1):
        print(k+1, end=" ")
    print("\r")