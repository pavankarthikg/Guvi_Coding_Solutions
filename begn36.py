s=input()
ct=0
for i in range (0,len(s)):
    if ((s[i].isalpha()!=1) and (s[i].isdigit()!=1)):
        ct+=1
print(ct)
