from collections import OrderedDict
s=str(input())
print("".join(OrderedDict.fromkeys(s)))
