# Python program to print perfect numbers from 1 to 1000
def perfect_Number(n):  #user-defined function
   if n < 1:
      return False

   perfect_sum = 0
   for i in range(1,n):
      if n%i==0:
         perfect_sum += i
   return perfect_sum == n

# take inputs
min_value = 1
max_value = 1000

# calling function and print perfect numbers
print('Perfect numbers from %d to %d are:' %(min_value, max_value))
for i in range(min_value, max_value+1):
   if perfect_Number(i):
      print(i, end=', ')