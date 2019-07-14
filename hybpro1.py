import os
N=int(input())
l=[]
for i in range(N):
    l.append(input())
print(os.path.commonprefix(l))
