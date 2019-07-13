n,k=map(int,input().split())
li=list(map(int,input().split()))[:n]
mos=int(input())
nij=(sum(li)-li[k])//2
if (nij==mos):
    print("Bon Appetit")
else:
    print(abs(nij-mos))
