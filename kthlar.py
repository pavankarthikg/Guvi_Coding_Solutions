N,k = [int (n) for n in input().split()]
s=list(map(int,input().split()))[:N]
s.sort(reverse=True)
print(s[k-1])
