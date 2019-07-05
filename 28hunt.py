s=str(input())
l=len(s)
for i in range (0,l-1):
    for j in range (i+1,l):
        if(s[i]==s[j]):
            f.append(a[i])
    
