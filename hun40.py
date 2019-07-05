a=str(input())
l=len(a)
sum=0
for i in range (0,l):
    sum=sum+int(a[i])
x=str(sum)
y=x[::-1]
if(x==y):
    print("YES")
else:
    print("NO")
