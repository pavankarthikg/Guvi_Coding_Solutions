from itertools import permutations
pr=list(input())
fin=permutations(pr,len(pr))
for i in list(fin):
    print("".join(i))
