n,k=map(int,input().split())
li=list(map(int,input().split()))[:n]
ct=0
for i in range (0,len(li)-1):
  for j in range (i+1,len(li)):
    if (li[i]-li[j]==k) or (li[j]-li[i]==k):
      ct+=1
print(ct)
