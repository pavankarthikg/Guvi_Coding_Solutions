a,b=map(int,input().split())
ct=0
l=list(map(int,input().split()))[:a]
for i in range(0,a-1):
    for j in range (i+1,a):
        if ((l[i]+l[j])==b):
            ct+=1
if(ct>0):
    print("YES")
else:
    print("NO")
        
    
