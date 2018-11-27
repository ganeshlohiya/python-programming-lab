# title : Factorial of given number
# Ganesh Lohiya
# M 36

def factorial(n):    # defining a function 
 f=1
 if n<0:
  print("enter positive number")    # factorial can not be calculated for negative no.
 elif n==0 or n==1:
  print('1')    # factorial of 0 and 1 is 1
 else:  
  while n>1:
   f=f*n     # for multiplying all the numbers
   n=n-1     # bringing each value
  print(f)
x=int(input())
factorial(x)
