#title : Armstrong number
#Ganesh Lohiya
#M 36

def armstrong_no(x):
 s=0
 z=x      #save x in z
 while x>0:
  y=x%10     #y is stored as remainder of x when divided by 10
  s+=y**3     #take cube of remainder and add it to s
  x=x//10      #x is now stored as quetiont of x after dividing by 10
 print(s)      #repeat this process till last digit
 if s==z:
  print("Armstrong number")     #if final x is same as z 
 else:
  print("not an armstrong number")    # if not
b=int(input())
armstrong_no(b)
