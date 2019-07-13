import string
s=str(input())
alphabet = set(string.ascii_lowercase)   
def ispangram(string): 
    return set(string.lower())>= alphabet  
if(ispangram(s) == True): 
    print("yes") 
else: 
    print("no") 
