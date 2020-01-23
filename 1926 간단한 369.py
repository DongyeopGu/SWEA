N = int(input())                            
N_l = list(map(str, (range(1,N+1))))
count = 0
for i in N_l:
    count = i.count('3') + i.count('6') + i.count('9')
    if count == 1:
        print('-', end=' ')
    elif count == 2:
        print('--', end=' ')
    else:
        print(i, end=' ')
