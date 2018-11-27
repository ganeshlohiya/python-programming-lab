# Title : Fibonaki Series
# Ganesh Lohiya
# M 36

def fibonaki(n):   #defining a function 
 a=0
 b=1
 l=[]            #introducing blank list
 if n<0:
  print("enter positive number")     # fibonaki series cannot be calculated for negative number
 elif n==0:
  print('0')  
 elif n==1:
  print('0,1')
 else:
  l.append(a)  # append a and b in list l
  l.append(b)
  for i in range (n-2):
   f=a+b #fibonaki series logic
   l.append(f) # append all the numbers in the list till the the loop exits
   a=b  #let each number take its next value
   b=f
  print(l)
a=int(input())
b=fibonaki(a)
print(b)
