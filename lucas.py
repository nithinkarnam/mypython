a=0
b=0
c=1 
n=int(input())
print(a)
print(b)
print(c)
for i in range(3,n):
    n3=a+b+c 
    a=b 
    b=c 
    c=n3 
    print(n3)
