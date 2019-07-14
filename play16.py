s=int(input())
li=list(map(int,input().split()))[:s]
for i in li:
    if li.count(i)==1:
        m=i
print (m)
