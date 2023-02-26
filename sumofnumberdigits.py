x=[]
n=int(input('enter range'))
for i in range(0,n):
  e=int(input('enter elements of list'))
  x.append(e)
s=0
for i in x:
  if i.isdigit()==True:
    s+=int(i)
    print('sum of digits',s)
    
