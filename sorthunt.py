a=[]
s=[]
f=[]
x=int(input())
a=list(map(int,input().split()))[:x]
def dif(l1,l2):
    dif= [i for i in l1 + l2 if i not in l1 or i not in l2]
    return dif
for i in range(0,x-1):
    for j in range ((i+1),x):
        if(a[i]==a[j]):
            s.append(a[i])
f=dif(a,s)
print(*f)
