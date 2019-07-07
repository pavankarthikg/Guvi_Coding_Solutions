n=int(input())
s=str(n)
l=len(s)
sum=0
for i in range (0,l):
    sum=sum+(int(s[i])**i)
print(sum)
