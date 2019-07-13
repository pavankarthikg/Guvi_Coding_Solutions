n=int(input())
l=list(map(int,input().split()))[:n]
f=[]
mx=sorted(l)
mn=mx[::-1]
for i in range (0,n//2):
    f.append(mn[i])
    f.append(mx[i])
print(*f,sep=" ")
    

        
        
        
