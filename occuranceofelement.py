n=int(input())
x=list()
for i in range(n):
  e=input("enter element %d"%(i+1))
  x.append(e)
  d=dict()
  for i in x:
    d[i]=x.count(i)
   fori in d:
    print(i,d[i])
