s=str(input())
v=('a','e','i','o','u')
if(s.isalpha())==True:
    if(s.lower() in v):
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid")
