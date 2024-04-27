import random
import string
def genearte_password(len,complexity):
    if complexity=="low":
        char=string.ascii_lowercase+string.digits
    elif complexity=="medium":
        char=string.ascii_letters+string.digits
    elif complexity=="high":
        char=string.ascii_letters+string.digits+string.punctuation
    else:
        print("invalid complexity.Using default high")
        char=string.ascii_letters+string.digits+string.punctuation
    i=''.join(random.choice(char) for _ in range(len))
    return i
#main
print("\t\t\tWELCOME TO PASSWORD GENERATOR\n")
len=int(input("Enter the length of password you want:"))
complexity=input("Enter the complexity of password you want(low/medium/high):")
password=genearte_password(len,complexity)
print("generated password",password)