nu=int(input())
while nu%10==0:
  nu=nu//10
nu=str(nu)
re=nu[::-1]
if nu==re:
  print("yes")
else:
    print("no")
