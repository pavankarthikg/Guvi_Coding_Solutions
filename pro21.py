n=int(input())
l=list(map(int,input().split()))[:n]
p=len(l)//2
ct=0
x=l[p:]
y=l[:p]
if (sum(x)//len(x))==(sum(y)//len(y)):
    ct=1
if(ct==1):
    print("yes")
else:
    print("no")
