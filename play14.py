n=int(input())
s=str(input())
s=list(s)
for i in s:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        s.remove(i)
o=s[::-1]
print("".join(o))
