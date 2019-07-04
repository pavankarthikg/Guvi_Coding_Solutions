s1,s2=map(str,input().split())
d=0
for i in range (0,len(s1)):
    if(s1[i]!=s2[i]):
        d+=1
if (d==1):
    print("yes")
else:
    print("no")
