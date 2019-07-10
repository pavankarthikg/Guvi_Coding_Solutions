n,k=map(int,input().split())
a=str(n)
fin=a
for i in range(0,len(a)-1):
    for j in range (0,k+1):
        if (a[i]>a[i+1]):
            fin=a.replace(a[i],'')
print(fin)
