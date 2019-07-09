n=int(input())
l=list(map(int,input().split()))[:n]
ct=0
fin=[]
for i in range (0,n):
    fin.append((i+1)*n)
    for j in range (0,n):
        if (fin[i]==l[j]):
            ct+=1   
print(ct)       
        

