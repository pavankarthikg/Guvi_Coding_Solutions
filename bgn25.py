n=int(input())
li=list(map(int,input().split()))[:n]
li.sort()
print(*li)
