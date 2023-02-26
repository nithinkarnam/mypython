x=[]
n=input()
for i in range(0,n):
e=int(input("enter elements of a list"(i+1))
      x.append(e)
      d=dict()
      for i in x:
      d[i]=x.count(i)
      print('Duplicates',end='')
      for i in d:
      if d[i]>1:
      print(i,end='')
