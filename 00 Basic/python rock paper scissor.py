import random
while True:
    user= input('Rock(R) paper(P) or scissor(S) or End(E)')
    computer = ['R','P','S']
    cc= random.choice(computer)
    if (user=='R' and cc=='S') or (user == 'P' and cc== 'R') or (user == 'S' and cc=='P'):
        print('You win')
    elif user==cc:
        print('Draw')
    elif (user=='S' and cc=='R') or (user == 'R' and cc== 'P') or (user=='P' and cc=='S'):
        print('you lose')
    elif user == 'E':
        break
