import math
n,k=map(int,input().split())
a=list(map(int,input().split()))[:n]
s=[]
for i in range (0,k):
    l,r=map(int,input().split())
    s.append([l,r])
for i in s:
    le=i[0]-1
    ri=i[1]-1
    print(math.gcd(a[le],a[ri]))
    
