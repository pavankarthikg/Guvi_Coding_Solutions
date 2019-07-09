n,a,b=map(int,input().split())
ct=0
for i in range (0,n):
    if n>2:
        if ((a+b)*i)==n//2:
            ct+=1  
    if (n==2):
        if ((a+b)*i)==2:
            ct+=1             
if (ct==1):
    print("YES")
else:
    print("NO")
