while True:
    inp=input('Enter a number: (e for exit)')
    if inp == 'e':
        break
    a=int(inp)
    i=2
    while i < a:
        check = a%i
        if check == 0:
            r='p'
            break
        else:
            r='np'
            i=i+1
    if r=='p':
        print('Not prime')
    else:
        print('Prime')

    

    
