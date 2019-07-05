n,m=map(int,input().split())
for i in range(n,m):
    sum=0
    temp=i
    while (temp!=0):
        d=temp%10
        sum=sum+(d * d * d)
        temp=temp//10  
        if(i==sum):
            print(i, end=" ")
    

    

