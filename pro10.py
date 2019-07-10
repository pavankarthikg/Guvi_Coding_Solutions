n=int(input())
li=list(map(int,input().split()))[:n]
s=0
for i in range (0,n):
    for j in range (0,i):
        if (li[i]>li[j]):
            s=s+li[j]
print(s)
