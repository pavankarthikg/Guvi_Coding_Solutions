n=int(input())
ct=0
for i in range (0,n+1):
    s=str(i)
    for j in range (0,len(s)):
        if (s[j]=='2'):
            ct+=1
print(ct)        
