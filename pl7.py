st=str(input())
s=list(st)
for i in range(0,len(s)-1,2):
    temp=s[i+1]
    s[i+1]=s[i]
    s[i]=temp
print(*s,sep="")
