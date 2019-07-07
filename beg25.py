import statistics
n=int(input())
li=list(map(int,input().split()))[:n]
print(statistics.median(li))
