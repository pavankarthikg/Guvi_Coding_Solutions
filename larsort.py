N=int(input())
l=list(map(int, input().split()))[:N]
l.sort(reverse=True)
print(''.join(str(num) for num in l))
