N=int(input())
s=[]
g = list(map(int,input().split()))[:N]
for i in range(0,N):
    for j in range((i+1),N):
        if(g[i]==g[j]):
            s.append(g[i])
s.sort()
if(len(s)==0):
    print("unique")
else:
    print(*s,sep=" ")
 
    


            
