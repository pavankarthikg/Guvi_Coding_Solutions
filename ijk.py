N=int(input())
a= list(map(int,input().split()))[:N]
for i in range (0,(N-2)):
    for j in range (1, (N-1)):
        for k in range (2,N):
            if ((i<j)and (j<k)):
                sum=a[i]+a[j]
                if(sum==a[k]):
                    print(a[i] , a[j], a[k])
