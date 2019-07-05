N=int(input())
a=list(map(int, input().split()))[:N]
for i in range (0,N):
    if (i%2)!=0:
        if (a[i]%2)==0:
            print(a[i], end=' ')
        else:
            break
    else:
        if (a[i]%2)!=0:
            print(a[i], end=' ')
