s=str(input())
l=list(s)
x=f=[]
for i in range (0,len(s)-1):
    for j in range (i+1,len(s)):
        if (s[i]==s[j]):
            x.append(s[i])
f=list(set(l)-set(x))
f=sorted(f)
print(*f,sep="")
