n=int(input())
l=[]
li=list(map(int,input().split()))[:n]
for i in range (0,len(li)):
  l.append(li[i])
  l.sort()
  print(li[0],end=" ")
