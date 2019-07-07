a,b=map(str,input().split())
l=[]
for i in range (len(b)):
    if (a[i]==b[i]):
        l.append(a[i])
print(''.join(l))
