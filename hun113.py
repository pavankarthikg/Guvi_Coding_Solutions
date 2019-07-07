n=int(input())
ct=0
for i in range (0,n):
    if(n==2**i):
        ct=1
if(ct>0):
    print("YES") 
else:
    print("NO")
   
