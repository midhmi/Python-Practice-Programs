#to find out all divisor
#modulus = 0
a = input('Enter a number')
for i in range(int(a)-1):
    j=i+1
    if int(a)%j == 0:
        print(j)
