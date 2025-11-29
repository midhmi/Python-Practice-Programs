a= input('Enter any text')
b= len(a)
pal=''
for i in range(b):
    pal=a[b-i-1] + pal
if a == pal:
    print(a+' is palindrome')
else:
    print(a+' is not a palindromw')
    
