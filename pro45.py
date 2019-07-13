nu=input()
s1=nu[::-1]
ct=0
for i in range (0,len(nu)):
    if nu[i]==s1[i]:
        ct+=1
if ct==len(nu):
    print("yes")
else:
    print("no")
