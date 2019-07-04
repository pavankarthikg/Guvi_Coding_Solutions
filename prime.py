N=int(input())
s=[]
for i in range(1,N):
    if ((N%i)==0):
        s.append(i)
if(len(s)<=2):
    print("yes")
else:
    print("no")
