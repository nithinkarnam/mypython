n=int(input())
x=list()
for i in range(n):
  e=float(input("enter element %d"%(i+1)))
  x.append(e)
for i in x:
  if i>=0:
    print(i)
    
