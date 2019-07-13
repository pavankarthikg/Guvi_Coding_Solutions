s1,s2=map(str,input().split())
n=len(s1)
ct=0
for i in range (0,n):
    for j in range (0,len(s2)):
        if s1[i]==s2[j]:
            ct+=1      
if ct>=2:
    print("yes")
else:
    print("no")
