N=eval(input())
a=list(map(eval,input().split()))[:N]
for i in range(0,N-1):
    for j in range(1,N):
        if (a[i]+a[j]==0):
            print(a[i] , a[j])
        elif  ((a[i]+a[j]<0.4) and (a[i]+a[j]>0)):
            print(a[i] , a[j])
        elif ((a[i]+a[j]>-0.4) and (a[i]+a[j]<0)):
            print(a[i] , a[j])
        
