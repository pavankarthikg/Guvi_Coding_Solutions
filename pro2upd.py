from itertools import combinations
n,k=map(int,input().split())
l=len(str(n))
a=list(combinations(str(n),l-k))
a=sorted(a)
print(*a[0],sep='')
