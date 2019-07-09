n,a,b=map(int,input().split())
l=n//2
ct=0
for i in range (0,9999999):
    if ((a+b)*i==l or (a+b)*i==n):
        ct+=1
if (ct==1):
    print("YES")
else:
    print("NO")
