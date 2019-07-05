n,k=map(int,input().split())
li=list(map(int, input().split()))[:n]
c=0
for i in range (0,n-1):
    for j in range (i+1,n):
        if (li[i]+li[j]==k) :
            c+=1
if (c>0):
    print("yes")
else:
    print("no")
            
    
