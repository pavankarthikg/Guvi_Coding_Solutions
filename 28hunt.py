s=str(input())
l=len(s)
count=0
for i in range (0,l-1):
    for j in range (i+1,l):
        if(s[i]==s[j]):
            count+=1
        else:
            count=0
if (count>=0):
    print(s[i])
    
