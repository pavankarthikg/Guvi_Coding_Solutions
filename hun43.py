s=input()
fin=''
for i in range(0,len(s)-1,2):
  if int(s[i+1])%2==0:
    fin+=s[i]*int(s[i+1])
  else:
    fin+=s[i]+s[i+1]
print(fin)

