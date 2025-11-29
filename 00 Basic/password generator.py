import random
import string
e=''
for i in range(0,3,1):
    a=random.choice(string.digits)
    b=random.choice(string.ascii_lowercase)
    c=random.choice(string.ascii_uppercase)
    d=random.choice(string.punctuation)
    e=e+a+b+c+d

print(e)


