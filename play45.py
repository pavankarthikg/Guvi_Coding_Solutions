s=input()
ct=0
for i in s:
    if s.count(i)>ct:
        ct=s.count(i)
        fin=i
print(fin)
