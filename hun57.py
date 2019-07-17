n=int(input())
li=list(map(int,input().split()))[:n]
for i in range (0,len(li)):
  if li.count(li[i])==1:
    print(li[i])
