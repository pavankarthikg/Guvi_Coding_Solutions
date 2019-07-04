N, M = [int(N) for N in input().split()] 
a=list(map(int,input().split()))[:N]
b=list(map(int,input().split()))[:M]
if ((set(b) & set(a))==set(b)):
    print("YES")
else:
    print("NO")
