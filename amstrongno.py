def armstrong_no(x):
 s=0
 z=x
 while x>0:
  y=x%10
  s+=y**3
  x=x//10
 print(s)
 if s==z:
  print("armstrong number")
 else:
  print("not an armstrong number")
b=int(input())
armstrong_no(b)
