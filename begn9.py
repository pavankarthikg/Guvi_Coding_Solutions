N,k=map(int,input().split())
sum=0
s=list(map(int,input().split()))[:N]
for i in range (0,k):
    sum=sum+s[i]
print(sum)
