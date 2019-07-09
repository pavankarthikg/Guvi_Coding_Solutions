n=int(input())
l=[]
dif=0
for i in range (0,n+1):
    dif=abs((2**i)-n)
    l.append(dif)
x=min(l)
print(x)
    
