def amstrong_no(x):
 s=0
 z=x
 while x>0:
  y=x%10
  s+=y**3
  x=x//10
 print(s)
 if s==z:
  print("amstrong number")
 else:
  print("not an amstrong number")
b=int(input())
a=amstrong_no(b)
print(a)
