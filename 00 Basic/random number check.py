import random
r=random.randint(1,9)

while True:
    a=int(input('Enter a random number '))
    if a==r:
        print(str(a)+'is Correct random number ie '+str(r))
        break
    elif a>r:
        print('High')
    else:
        print('Low')
