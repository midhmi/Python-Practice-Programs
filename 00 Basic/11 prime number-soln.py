a=1
b=1
r=int(input('Enter the maximum up to which the series is to calcilated'))
print(a)
print(b)
while b<=r:
    c=a+b
    if c<=r:
        print(c)
    a=b
    b=c


