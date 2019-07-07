n=int(input())
l=list(map(int,input().split()))[:n]
ct=0
for i in range(0,n-1):
    for j in range(i+1,n):
        if(l[i]<l[j]):
            ct+=1
print(ct)
