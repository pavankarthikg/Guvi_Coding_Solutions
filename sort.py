a=[]
s=[]
x=int(input())
a=list(map(int,input().split()))[:x] 
for i in range(0,x):
    if (a[i]==i):
        s.append(a[i])
        s.sort()
if(len(s)>0):
    print(*s,sep=" ")
else:
    print(-1)
    
        

        
