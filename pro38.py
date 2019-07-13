n,k=map(int,input().split())
li=list(map(int,input().split()))[:n]
ct=0
for i in range (0,n):
    if (li[i]+k)<=5:
        ct+=1
print(ct//3)
