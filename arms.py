n=int(input())
temp=int(n)
sum=0
while (temp!=0):
    d=temp%10
    sum=sum+(d * d * d)
    temp=temp//10
if(n==sum):
    print("yes")
else:
    print("no")
    
    
