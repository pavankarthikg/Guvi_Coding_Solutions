n=int(input())
li=[]
fin=[]
for i in range (0,n):
    li=list(map(int, input().split()))
    for j in li:
        fin.append(j)
a=sorted(fin)
print(*a, end="")
    
