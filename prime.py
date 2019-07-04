N=int(input())
s=[]
for i in range(1,N+1):
    if ((N%i)==0):
        s.append(i)
if(len(s)>2):
    print("no")
else:
    print("yes")
