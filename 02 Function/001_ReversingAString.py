# Reverse a String 
def rev_string(c):
    d = ""
    for x in c:
        d = x+d
    return d

c = input("Enter a string")
l = len(c)

print(rev_string(c))
