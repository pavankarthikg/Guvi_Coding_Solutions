x=int(input())
lis=list(map(int,input().split()))[:x]
lis.sort()
print(*lis,sep=' ')
