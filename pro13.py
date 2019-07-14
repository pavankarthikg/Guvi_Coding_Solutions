n,q=map(int,input().split())
li=list(map(int,input().split()))[:n]
l=[]
for _ in range (0,q):
    u,v=map(int,input().split())
    l.append(min(li[u-1:v]))
for i in l:
    print(i)
