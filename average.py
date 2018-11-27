total=0
n=0
count=0
while n>=0:
  total+=n
  count+=1
  n=int(input())
avg=total/(count-1)
print(avg)