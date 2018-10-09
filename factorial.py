def factorial(n):
 f=1
 if n<0:
  print("enter positive number")
 elif n==0 or n==1:
  print('1')
 else:  
  while n>1:
   f=f*n
   n=n-1
  print(f)
x=int(input())
factorial(x)
